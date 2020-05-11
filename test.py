from contextlib import contextmanager

n = 0


@contextmanager
def foo():
    global n
    n += 1
    yield
    n -= 1


def bar():
    with foo():
        for _ in range(5):
            print(n)
            return
print(bar())
print(n)
