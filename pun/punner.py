from .echo import echo, fail, success
from .core import Task


class Punner(object):
    def __init__(self, punfile):
        self.punfile = punfile
        self.puntasks = []
        self.default = getattr(self.punfile, 'DEFAULT', None)

    def get_tasks(self):
        for item in dir(self.punfile):

            it = getattr(self.punfile, item)
            if isinstance(it, Task):
                self.puntasks.append(it)

    def setup(self):
        self.get_tasks()

    def run(self, tasks):
        if not tasks:
            if self.default is not None:
                runner(self.default, self.punfile)
            else:
                helper(self.puntasks)

        else:
            to_run = [self.get(task) for task in tasks]
            runner(to_run, self.punfile)

    def get(self, key):
        for puntask in self.puntasks:
            if puntask.meta['name'] == key:
                return puntask
        else:
            print('No target', key)


def runner(task_list, pf=None):
    """
    Run execute_task on each task
    """

    if isinstance(task_list, list):
        for t in task_list:
            execute_task(t, pf)

    else:
        execute_task(task_list, pf)


def execute_task(t, pf):
    """
    Execute a given task
    """

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


def helper(task_list):
    """
    Show help of each task
    """

    for t in task_list:
        echo(t.meta['name'], t.meta['desc'])
