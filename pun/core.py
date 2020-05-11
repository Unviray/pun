from collections import namedtuple
from functools import wraps
from subprocess import call
from typing import List

from .echo import echo, fail, success


Task = namedtuple('Task', ['func', 'meta'])


def task(*required, **kwargs):

    def deco(func):

        @wraps(func)
        def wraped():
            return func()

        meta = {
            'required': required,
            'name': func.__name__,
            'desc': func.__doc__.strip(),
        }

        return Task(wraped, meta)

    return deco


def run(*args):
    arg = ' '.join(args).split(' ')
    call(arg)


def execute_task(t, pf):
    if isinstance(t, str):
        t = getattr(pf, t)

    try:
        required = t.meta['required']

        if required:
            for req in required:
                runner(req, pf)

        t.func()

    except Exception as e:
        fail(e, t.meta['name'])
    else:
        success(t.meta['name'])


def runner(task_list, pf=None):
    if isinstance(task_list, list):
        for t in task_list:
            execute_task(t, pf)

    else:
        execute_task(task_list, pf)


def helper(task_list):
    for t in task_list:
        echo(t.meta['name'], t.meta['desc'])
