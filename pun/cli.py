# -*- coding: utf-8 -*-

import sys
from importlib.util import spec_from_file_location

import click

from .walker import find_punfile
from .utils import import_string
from .core import Task, runner, helper


@click.command()
@click.argument('task', nargs=-1)
def main(task):
    # find punfile
    punfile = find_punfile()
    if punfile is None:
        sys.exit(1)

    # import punfile
    sys.path.append(punfile.parent)
    import punfile as pf

    # retrive task
    all_task = []
    for item in dir(pf):
        it = getattr(pf, item)
        if isinstance(it, Task):
            all_task.append(it)

    default = getattr(pf, 'DEFAULT')

    if not task:
        if default:
            runner(default, pf)
        else:
            helper(all_task)

    # filter task based on argument
    def flt(t):
        return t.meta['name'] in task

    target_task = list(filter(flt, all_task))

    # run filtered task
    runner(target_task, pf)

    sys.exit(0)
