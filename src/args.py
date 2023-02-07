# pylint: disable=missing-module-docstring

import json
import argparse
from rich.traceback import install

install()


class PayloadCheck(argparse.Action):
    """Payload JSON check"""

    def __call__(self, parser, args, values, option_string=None):
        """Try to load JSON"""

        setattr(args, self.dest, json.loads(values))
