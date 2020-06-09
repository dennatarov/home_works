# Задача-1
# Создать объект менеджера контекста который будет переходить в папку которую он принимает на вход.
# Так же ваш объект должен принимать исключение которое он будет подавлять.
# Если флаг об исключении отсутствует, исключение должно быть поднято.

import os

class GoToDir:
    def __init__(self, dir_go_to, *exception):
        self.dir_go_to = dir_go_to
        self.current_dir = os.getcwd()
        self.exception = exception

    def __enter__(self):
        try:
            os.chdir(self.dir_go_to)
        except self.exception as e:
            print("An error was suppressed.", e.__doc__)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.current_dir)


# with GoToDir("C:/New/Primary/1.txt", NotADirectoryError) as n_dir:
#     file = open("1.txt", 'w')
#     file.close()

# Задача-2
# Описать задачу выше но уже с использованием @contextmanager.

from contextlib import contextmanager

@contextmanager
def go_to_dir(dir_go_to, *exception):
    current_dir = os.getcwd()
    try:
        os.chdir(dir_go_to)
        yield
    except exception as e:
        print("An error was suppressed.", e.__doc__)
        yield
    finally:
        os.chdir(current_dir)


# with go_to_dir("C:/New/Primary/01/", FileNotFoundError) as n_dir:
#     file = open("1.txt", 'w')
#     file.close()

# Задача-3
# Создать менеджер контекста который будет подсчитывать время выполнения вашей функции.

from time import monotonic

class FuncTimer:
    def __enter__(self):
        self.s_time = monotonic()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Execution time is {} s".format(monotonic() - self.s_time))

def fib(n):
    """Returns n-th Fibonacci number"""
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

with FuncTimer():
    fib(10)