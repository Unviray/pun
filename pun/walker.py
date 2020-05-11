import os
from contextlib import contextmanager
from pathlib import Path

from .config import Config


def here():
    """
    Return current working directory.
    """

    return Path()


@contextmanager
def cd(target_dir):
    """
    Change working directory.
    """

    cwd = here().resolve()

    try:
        os.chdir(Path(target_dir))
        yield
    finally:
        os.chdir(cwd)


def find_punfile():
    for n in range(Config().PARENT_LEN):
        with cd('../' * n):
            if Path('punfile.py') in here().iterdir():
                return Path('punfile')

    print('Unable to find punfile')
