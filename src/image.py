# pylint: disable=missing-module-docstring

from pathlib import Path

from requests import Response
from rich.traceback import install

install()


# pylint: disable=too-few-public-methods
class Image:
    """Image related functionality"""

    image_output_directory = Path("/output")

    @staticmethod
    def save_image_from_response(response: Response, file_name: str) -> None:
        """Save image file from Response"""
        with open(file_name, "wb") as image_file:
            image_file.write(response.content)
