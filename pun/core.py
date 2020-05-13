"""
pun.core
========

Main functionality of pun.
"""

from collections import namedtuple
from functools import wraps
from subprocess import run as call


Task = namedtuple('Task', ['func', 'meta'])
Fixt = namedtuple('Fixt', ['func', 'meta'])


def task(*required, **kwargs):
    """
    Decorate function with it to make a task
    """

    def deco(func):

        @wraps(func)
        def wraped(*a, **k):
            return func(*a, **k)

        if func.__doc__ is None:
            func.__doc__ = ''

        meta = {
            'required': required,
            'name': kwargs.get('name', func.__name__),
            'desc': kwargs.get('desc', func.__doc__.strip()),
            'hide': kwargs.get('hide', False)
        }

        return Task(wraped, meta)

    return deco


def fixture(func):

    @wraps(func)
    def wraped(*args, **kwargs):
        return func(*args, **kwargs)

    if func.__doc__ is None:
        func.__doc__ = ''

    meta = {
        'name': func.__name__,
        'desc': func.__doc__.strip(),
    }

    return Fixt(wraped, meta)


def run(*args):
    """
    Run a command. ex: python setup.py install
    """

    if callable(args[0]):
        return args[0](*args[1:])

    args = [str(_) for _ in args]
    arg = ' '.join(args).split(' ')
    process = call(arg)

    if process.stdout is not None:
        print(process.stdout)

    process.check_returncode()
