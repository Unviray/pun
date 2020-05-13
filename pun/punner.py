import re
import sys

from .echo import echo, fail, success
from .core import Task, Fixt


class Punner(object):
    def __init__(self, punfile):
        self.punfile = punfile
        self.puntasks = []
        self.fixtures = []
        self.default = getattr(self.punfile, 'DEFAULT', None)

    def init_tasks(self):
        for item in dir(self.punfile):

            it = getattr(self.punfile, item)
            if isinstance(it, Task):
                self.puntasks.append(it)

    def init_fixtures(self):
        for item in dir(self.punfile):

            it = getattr(self.punfile, item)
            if isinstance(it, Fixt):
                self.fixtures.append(it)

    def setup(self):
        self.init_tasks()
        self.init_fixtures()

    def run(self, tasks):
        if not tasks:
            if self.default is not None:
                self.runner(self.default)
            else:
                helper(self.puntasks)

        else:
            to_run = []
            for task in tasks:
                t = self.get_task(task)
                if t is not None:
                    to_run.append(t)

            self.runner(to_run)

    def get_task(self, key):
        for puntask in self.puntasks:
            if puntask.meta['name'] == key:
                return puntask
        else:
            print('No target', key)
            sys.exit(2)

    def get_fixture(self, key):
        for fixture in self.fixtures:
            if fixture.meta['name'] == key:
                return fixture
        else:
            print('No fixture', key)
            sys.exit(2)

    def runner(self, task_list):
        """
        Run execute_task on each task
        """

        if isinstance(task_list, list):
            for t in task_list:
                self.execute_task(t)

        else:
            self.execute_task(task_list)

    def execute_task(self, t):
        """
        Execute a given task
        """

        if isinstance(t, str):
            t = getattr(self.punfile, t)

        try:
            required = t.meta['required']
            if required:
                for req in required:
                    self.runner(req)

            try:
                t.func()
            except TypeError as e:
                fixtures = self.get_required_fixtures(e)
                t.func(*fixtures)

        except Exception as e:
            fail(e, t.meta['name'])
            sys.exit(1)
        else:
            success(t.meta['name'])

    def get_required_fixtures(self, type_error):
        f_error = str(type_error)

        n = re.compile(r'\s[1-9]\s|\s[1-9]{2}\s')
        n = n.findall(f_error)[0].split(' ')[1]

        fixtures = re.compile(r"'[a-zA-Z_]*'")
        fixtures = fixtures.findall(f_error)
        fixtures = [_.split("'")[1] for _ in fixtures]

        return [self.get_fixture(_).func for _ in fixtures]


def helper(task_list):
    """
    Show help of each task
    """

    for t in task_list:
        echo(t.meta['name'], t.meta['desc'])
