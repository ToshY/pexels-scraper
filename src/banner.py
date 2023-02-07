# pylint: disable=missing-module-docstring

import pyfiglet
from rich.console import Console

console = Console()


def cli_banner(
    banner_title: str,
    banner_font: str = "big",
    banner_color: str = "bold green",
    banner_width: int = 100,
) -> None:
    """CLI banner"""

    banner = pyfiglet.figlet_format(banner_title, font=banner_font, width=banner_width)
    console.print(banner, style=banner_color, highlight=False)
