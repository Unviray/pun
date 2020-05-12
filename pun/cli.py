"""
pun.cli
=======

Entry of console.
"""

import sys

import click

from .walker import find_punfile
from .punner import Punner


@click.command()
@click.argument('tasks', nargs=-1)
def main(tasks):
    punfile_path = find_punfile()
    if punfile_path is None:
        sys.exit(1)

    punfile = import_punfile(punfile_path)

    punner = Punner(punfile)
    punner.setup()
    punner.run(tasks)


def import_punfile(pun_path):
    sys.path.append(pun_path.parent)
    import punfile as pf

    return pf
