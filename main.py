# pylint: disable=missing-module-docstring

import sys
import argparse
from argparse import Namespace
import logging
from rich.traceback import install
from rich.console import Console
from src.api import PexelsAPI
from src.banner import cli_banner
from src.args import PayloadCheck

console = Console()
install()


def cli_args() -> Namespace:
    """Parse command line arguments"""

    parser = argparse.ArgumentParser(
        description="A python command-line tool for scraping images from Pexels.com by topic search.",
        epilog="Repository: https://github.com/ToshY/pexels-scraper",
    )
    parser.add_argument(
        "-k",
        "--key",
        help="API key.",
        dest="api_key",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-p",
        "--payload",
        help="Payload in JSON format.",
        dest="payload",
        action=PayloadCheck,
        type=str,
        required=True,
    )
    parser.add_argument(
        "-d",
        "--debug",
        help="Debug loglevel; Fallback to WARNING.",
        dest="loglevel",
        action="store_const",
        const=logging.DEBUG,
        default=logging.WARNING,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Info loglevel.",
        dest="loglevel",
        action="store_const",
        const=logging.INFO,
    )

    user_args = parser.parse_args()
    logging.basicConfig(
        format="%(levelname)s: %(message)s",
        level=user_args.loglevel,
    )

    return user_args


def main():
    """Get Pexels images"""
    args = cli_args()

    pexels_api = PexelsAPI(args.api_key)
    pexels_api.search_for_photos(args.payload)


if __name__ == "__main__":
    cli_banner("Pexels  Scraper")

    try:
        main()
    except KeyboardInterrupt:
        console.print("\r\n[red]Execution cancelled by user[/red]")
        sys.exit()
