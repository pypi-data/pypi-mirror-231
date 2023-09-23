import os
import shutil
import sys
import tarfile
import time
from copy import copy
from copy import deepcopy
from glob import glob
from subprocess import check_output
from subprocess import run
from tempfile import TemporaryDirectory
from threading import Thread

import requests
from requests_futures.sessions import FuturesSession

from nginx_updater.logger import logger
from nginx_updater.utils import get_expo_jitter


def compress(file_path, dir_path, excluded, packages):
    logger.info(f"Compressing to {file_path}...")
    file_dir_path = os.path.dirname(file_path)
    if file_dir_path:
        os.makedirs(file_dir_path, exist_ok=True)
    excluded = excluded + [".git", "dist", "venv", file_path]
    excluded = [os.path.normpath(e) for e in excluded]
    with tarfile.open(file_path, "w:bz2") as tar:
        for dirname, subdirs, files in os.walk(dir_path):
            # copy(subdirs) is used to make a copy of subdir, very important
            # to not bug the loop by subdirs.remove
            for subdir in copy(subdirs):
                file_path = os.path.join(dirname, subdir)
                rel_path = os.path.relpath(file_path, dir_path)
                if rel_path in excluded:
                    logger.info(f"Excluding dir {rel_path}...")
                    subdirs.remove(subdir)
            for basename in files:
                file_path = os.path.join(dirname, basename)
                rel_path = os.path.relpath(file_path, dir_path)
                if rel_path in excluded:
                    logger.info(f"Excluding file {rel_path}...")
                    continue
                tar.add(file_path, arcname=rel_path)
        site_packages = os.path.join(dir_path, "venv", "Lib", "site-packages")
        for p in packages:
            for file_path in glob(os.path.join(site_packages, p + "*")):
                rel_path = os.path.relpath(file_path, dir_path)
                tar.add(file_path, arcname=rel_path)


def remove_old_files(extract_dir, excluded):
    for name in glob(os.path.join(extract_dir, "*")):
        basename = os.path.basename(name)
        if basename in excluded + ["dist", "venv"]:
            continue
        try:
            if os.path.isfile(name) or os.path.islink(name):
                os.unlink(name)
            elif os.path.isdir(name):
                shutil.rmtree(name)
        except OSError:
            pass


def extract(file_path, extract_dir):
    os.makedirs(extract_dir, exist_ok=True)
    if file_path.endswith("tar.gz"):
        tar = tarfile.open(file_path, "r:gz")
        tar.extractall(extract_dir)
        tar.close()
    elif file_path.endswith("tar.bz2"):
        tar = tarfile.open(file_path, "r:bz2")
        tar.extractall(extract_dir)
        tar.close()
    elif file_path.endswith("tar"):
        tar = tarfile.open(file_path, "r:")
        tar.extractall(extract_dir)
        tar.close()
    shutil.copyfile(file_path + ".etag", os.path.join(extract_dir, "etag"))


def get_local_etag(file_path):
    try:
        with open(file_path) as fp:
            return fp.read()
    except OSError:
        return None


def post_download(session, data):
    headers = {}
    etag = get_local_etag(data["file_path"] + ".etag")
    headers = {"If-None-Match": etag}
    if "username" in data and "password" in data:
        auth = data["username"], data["password"]
    else:
        auth = None
    data["file"] = session.get(
        data["url"], headers=headers, auth=auth, stream=True, timeout=60
    )
    return data


def verify_archive(file_path):
    try:
        if file_path.endswith("tar.gz"):
            with TemporaryDirectory() as temp:
                tar = tarfile.open(file_path, "r:gz")
                tar.extractall(temp)
                tar.close()
                return True
        elif file_path.endswith("tar.bz2"):
            with TemporaryDirectory() as temp:
                tar = tarfile.open(file_path, "r:bz2")
                tar.extractall(temp)
                tar.close()
                return True
        elif file_path.endswith("tar"):
            with TemporaryDirectory() as temp:
                tar = tarfile.open(file_path, "r:")
                tar.extractall(temp)
                tar.close()
                return True
        else:
            return False
    except tarfile.TarError:
        return False


def write_file(data):
    response = data["file"].result()
    if response.status_code == 304:
        return response.status_code
    if not response.ok:
        return response.status_code
    file_path = data["file_path"]
    dir_path = os.path.dirname(file_path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(response.content)

    if not verify_archive(file_path):
        logger.info(f"{file_path} is not a valid archive.")
        print(1)
        return -1

    if "Etag" in response.headers:
        with open(file_path + ".etag", "w") as f:
            f.write(response.headers["Etag"])
    return response.status_code


def install_requirements(data):
    logger.info("Installing requirements using pip...")
    python = os.path.join(data["extract_dir"], "venv", "Scripts", "python.exe")
    if not os.path.exists(python):
        logger.info("No venv detected. Skipping...")
        return
    run(
        [python, "-m", "pip", "install", "-r", "requirements.txt"],
        cwd=data["extract_dir"],
    )


def sync(session, config):
    total = len(config)

    for data in config:
        post_download(session, data)

    for i, data in enumerate(config):
        code = write_file(data)
        logger.info(f"Syncing ({i+1}/{total}), Status Code: {code}...")


def check_for_updates(config, restart=True):
    logger.info("Checking for updates...")
    config = deepcopy(config)
    session = FuturesSession()
    sync(session, config)

    update_required = []
    for data in config:
        source_etag = get_local_etag(data["file_path"] + ".etag")
        dest_etag = get_local_etag(os.path.join(data["extract_dir"], "etag"))
        if source_etag is not None and source_etag != dest_etag:
            name = data["name"]
            logger.info(f"{name} has new updates.")
            update_required.append(data)

    if update_required == []:
        logger.info("Already upto date.")
        return

    total = len(update_required)
    for i, data in enumerate(update_required):
        remove_old_files(data["extract_dir"], data["exclude"])
        extract(data["file_path"], data["extract_dir"])
        logger.info(f"Extracting ({i+1}/{total})...")
        if data.get("install_requirements", False):
            install_requirements(data)

    if restart:
        os.execl(sys.executable, sys.executable, *sys.argv)


def check_for_updates_task(data, restart=True, interval=900, delay_first=900):
    time.sleep(delay_first)
    attempts = 0
    while True:
        try:
            check_for_updates(data, restart=restart)
            attempts = 0
            backoff = interval
        except requests.exceptions.RequestException:
            backoff = get_expo_jitter(
                5,
                attempts=attempts,
                cap=interval,
                jitter_min=5,
            )
            attempts += 1
            logger.info(f"Connection issues. Retrying in {backoff} seconds...")
        except Exception as exp:
            logger.error(f"Unhandled exception in updater: {exp}")
            attempts = 0
            backoff = interval
        time.sleep(backoff)


def start_check_for_updates_task(
    data, restart=True, interval=900, delay_first=900
):
    """Periodically updates the bot in a thread"""
    args = data, restart, interval, delay_first
    Thread(target=check_for_updates_task, args=args, daemon=True).start()


def upload(data, add_version=True, commit_as_version=False, run_scp=True):
    """
    :param commit_as_version: when set to True, uses git commit message as version
    :param run_scp: whether to do scp the dist file or not
    """
    version = None
    if add_version:
        if commit_as_version:
            version = check_output("git log -1 --oneline --format=%s").decode()
        else:
            version = input(
                "Enter a short description for this patch "
                "(Leave this blank to use last VERSION): "
            )

    data = deepcopy(data)
    for d in data:
        if version:
            with open(os.path.join(d["extract_dir"], "VERSION"), "w") as fp:
                fp.write(version)
        compress(
            d["file_path"],
            d["extract_dir"],
            d["exclude"],
            d.get("packages", []),
        )
        path = os.path.abspath(d["file_path"])
        if run_scp and "scp_executable" in d and "scp_destination" in d:
            logger.info(f'Uploading to {d["scp_destination"]}...')
            if os.path.isfile(d["scp_executable"]):
                run(
                    [
                        d["scp_executable"],
                        d["file_path"],
                        d["scp_destination"],
                    ]
                )
                logger.info("Success.")
            else:
                logger.info(f"File not found: {d['scp_executable']}")
        else:
            logger.info(
                "scp_executable and scp_destination is not set. Manually copy"
                f" {path}"
            )
