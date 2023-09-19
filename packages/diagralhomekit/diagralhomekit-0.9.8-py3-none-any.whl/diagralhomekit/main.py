# ##############################################################################
#  Copyright (c) Matthieu Gallet <github@19pouces.net> 2023.                   #
#  This file main.py is part of DiagralHomekit.                                #
#  Please check the LICENSE file for sharing or distribution permissions.      #
# ##############################################################################
"""All the main functions."""
import argparse
import logging
import os
import pathlib
import signal
import socket
import sys
import urllib.parse
from multiprocessing import Queue

import sentry_sdk
from logging_loki import LokiQueueHandler, emitter

# noinspection PyPackageRequirements
from pyhap.accessory import Bridge

# noinspection PyPackageRequirements
from pyhap.accessory_driver import AccessoryDriver

from diagralhomekit.config import HomekitConfig
from diagralhomekit.diagral import DiagralHomekitPlugin

logger = logging.getLogger("diagralhomekit")


def main():
    """parse arguments and run the daemons."""
    parser = argparse.ArgumentParser()
    default_port = int(os.environ.get("DIAGRAL_PORT", "51826"))
    default_config_dir = os.environ.get("DIAGRAL_CONFIG", "/etc/diagralhomekit")
    default_sentry_dsn = os.environ.get("DIAGRAL_SENTRY_DSN")
    default_loki_url = os.environ.get("DIAGRAL_LOKI_URL")
    verbosity = int(os.environ.get("DIAGRAL_VERBOSITY", 0))
    parser.add_argument(
        "--create-config",
        help="--create-config 'email:password' display a sample configuration file",
        default=None,
    )
    parser.add_argument("-p", "--port", type=int, default=default_port)
    parser.add_argument(
        "-C",
        "--config-dir",
        default=pathlib.Path(default_config_dir),
        type=pathlib.Path,
    )
    parser.add_argument("--sentry-dsn", default=default_sentry_dsn)
    parser.add_argument("--loki-url", default=default_loki_url)
    parser.add_argument("-v", "--verbosity", default=verbosity, type=int)
    args = parser.parse_args()
    config_dir = args.config_dir
    if args.create_config:
        login, sep, password = args.create_config.partition(":")
        if sep != ":":
            print("Usage: --create-config=login:password")
            return
        content = DiagralHomekitPlugin.show_basic_config(login, password)
        print(f"cat << EOF > {config_dir}/config.ini")
        print(content)
        print("EOF")
        return

    handler = logging.StreamHandler(sys.stdout)
    if args.verbosity == 0:
        logger.setLevel(logging.WARNING)
    elif args.verbosity == 1:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    listen_port = args.port

    if args.loki_url:
        try:
            hostname = socket.gethostname()
        except socket.gaierror:
            hostname = "localhost"
        emitter.LokiEmitter.level_tag = "level"
        parsed_url = urllib.parse.urlparse(args.loki_url)
        url = f"{parsed_url.scheme}://{parsed_url.hostname}"
        if parsed_url.port:
            url += f":{parsed_url.port}"
        url += parsed_url.path
        if parsed_url.query:
            url += f"?{parsed_url.query}"
        handler = LokiQueueHandler(
            Queue(-1),
            url=url,
            tags={
                "application": "diagralhomekit",
                "log_source": "diagralhomekit",
                "hostname": hostname,
            },
            auth=(parsed_url.username or "", parsed_url.password or ""),
            version="1",
        )
        logger.addHandler(handler)
        logger.debug("Loki configured.")

    if args.sentry_dsn:
        sentry_sdk.init(args.sentry_dsn)
        logger.debug("Sentry DSN configured.")

    run_daemons(
        config_dir,
        listen_port,
        verbosity=args.verbosity,
    )


def run_daemons(config_dir, listen_port, verbosity: int = 1):
    """launch all processes: Homekit and Diagral checker."""
    persist_file = config_dir / "persist.json"
    config_file = config_dir / "config.ini"
    logger.info(f"configuration file: {config_file}")
    logger.info(f"persistence file: {persist_file}")
    logger.info(f"listen port: {listen_port}")

    driver = AccessoryDriver(
        port=listen_port,
        persist_file=persist_file,
    )
    bridge = Bridge(driver, "Diagral e-One")
    config = HomekitConfig()
    config.verbosity = verbosity
    try:
        config.load_config(config_file)
        config.load_accessories(bridge)
        driver.add_accessory(accessory=bridge)
        signal.signal(signal.SIGTERM, driver.signal_handler)
        config.run_all()
        driver.start()
    except Exception as e:
        logger.exception(e)
        raise e
    config.stop_all()
