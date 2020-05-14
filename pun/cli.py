"""
pun.cli
=======

Entry of console.
"""

import click

from .walker import find_punfile
from .punner import Punner
from .config import Config
from .utils import import_file


@click.command()
@click.argument('tasks', nargs=-1)
def main(tasks):
    first_manager()

    punfile_path = find_punfile()

    if punfile_path is not None:
        with import_file(punfile_path) as p:
            punfile = p

        with import_file(Config().DEFAULT_PF) as p:
            default_pf = p

        punner = Punner(punfile)
        default_punner = Punner(default_pf)

        punner.setup()
        punner.setup(default_punner.punfile)

        punner.run(tasks)

    else:
        with import_file(Config().DEFAULT_PF) as p:
            default_pf = p

        default_punner = Punner(default_pf)

        default_punner.setup()
        default_punner.run(tasks)


def first_manager():
    """
    Check if first use and init pun.
    """

    home = Config().HOME

    if home.exists() and home.is_dir():
        return True

    from .first import default_punfile, config

    home.mkdir()

    punfile = Config().DEFAULT_PF
    conffile = Config().DEFAULT_CONFIG

    punfile.touch()
    conffile.touch()

    with punfile.open('wb') as fp:
        with open(default_punfile.__file__, 'rb') as tfp:
            fp.write(tfp.read())

    with conffile.open('wb') as fp:
        with open(config.__file__, 'rb') as tfp:
            fp.write(tfp.read())
