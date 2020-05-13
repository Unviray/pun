"""
pun.cli
=======

Entry of console.
"""

import sys
from importlib import import_module
from contextlib import contextmanager

import click

from .walker import find_punfile
from .punner import Punner
from .config import Config


@click.command()
@click.argument('tasks', nargs=-1)
def main(tasks):
    first_manager()

    punfile_path = find_punfile()

    if punfile_path is not None:
        with import_punfile(punfile_path) as p:
            punfile = p

        with import_punfile(Config().DEFAULT_PF) as p:
            default_pf = p

        punner = Punner(punfile)
        default_punner = Punner(default_pf)

        punner.setup()
        punner.setup(default_punner.punfile)

        punner.run(tasks)

    else:
        with import_punfile(Config().DEFAULT_PF) as p:
            default_pf = p

        default_punner = Punner(default_pf)

        default_punner.setup()
        default_punner.run(tasks)


@contextmanager
def import_punfile(pun_path):
    path_bak = sys.path[:]
    sys.path = [str(pun_path.parent)]

    try:
        pf = import_module(pun_path.name.split('.')[0])
        yield pf
    except ImportError:
        pass
    finally:
        sys.path = path_bak[:]


def first_manager():
    """
    Check if first use and init pun.
    """

    home = Config().HOME

    if home.exists() and home.is_dir():
        return True

    from .first import template

    home.mkdir()

    punfile = home / 'default_punfile.py'
    punfile.touch()

    with punfile.open('wb') as fp:
        with open(template.__file__, 'rb') as tfp:
            fp.write(tfp.read())
