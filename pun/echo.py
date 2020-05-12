"""
pun.echo
========

Print something in console.
"""

from click import style


def fail(msg, task_name=None, indent=25):
    title = style('[  fail  ]', fg='red')

    if task_name is not None:
        name = style(task_name, fg='bright_red', bold=True)
    else:
        name = ''

    n = name.ljust(indent)

    print(f'{title} {n} {msg}')


def success(task_name):
    title = style('[ success ]', fg='green')
    name = style(task_name, fg='bright_green', bold=True)

    print(f'{title} {name}')


def echo(task_name, msg, indent=25):
    name = style(task_name, bold=True)
    n = name.ljust(indent)

    print(f'{n} {msg}')
