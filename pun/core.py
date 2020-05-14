"""
pun.core
========

Main functionality of pun.
"""

import os
from contextlib import contextmanager
from collections import namedtuple
from functools import wraps
from subprocess import run as call


class Task(object):
    def __init__(self, func, meta):
        self.func = func
        self.meta = meta

    def clone(self, new_name):
        meta = self.meta.copy()
        meta['name'] = new_name

        return Task(self.func, meta)

    def __repr__(self):
        return f"<Task: {self.meta['name']}>"


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
            'as_option': kwargs.get('as_option', False),
        }

        meta['hide'] = kwargs.get('hide', True if meta['as_option'] else None)

        if meta['hide'] is None and meta['name'].startswith('_'):
            meta['hide'] = True

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


@contextmanager
def env(key, value):
    try:
        os.environ[key] = str(value)
        yield
    except Exception:
        pass
    finally:
        os.environ.pop(key)
