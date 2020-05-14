# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.

def task1_decor(func):
    def wrapper(*args):
        l = 100 % func(*args)
        if l == 0:
            print('We are ok!')
        else:
            print('Bad news guys, we got {}'.format(l))
    return wrapper

@task1_decor
def hw_func_01(s):
    return 2 * s + 1

print('Task 1')
hw_func_01(2)

# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))

def task2_decor(func):
    def wrapper(argument):
        if isinstance(argument, int):
            print(func(argument))
        elif isinstance(argument, str):
            raise ValueError('string type is not supported')
    return wrapper

@task2_decor
def hw_func_02(a):
    return a * 2

print('Task 2')
hw_func_02(2)

# ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
# количество раз обращений в cache.

def task3_decor(func):
    cache = {}
    counter_cache, counter_f = 0, 0
    def wrapper(*args):
        nonlocal counter_cache, counter_f
        if args in cache:
            counter_cache += 1
            print('Used cache with counter = {}'.format(counter_cache))
            return cache[args]
        else:
            cache[args] = func(*args)
            counter_f += 1
            print('Function executed with counter = {}, function result = {}'.format(counter_f, cache[args]))
            return cache[args]
    return wrapper

@task3_decor
def factorial(n):
    """ Calculation of Factorial n! """
    if n == 0: return 1
    return n * factorial(n - 1)

@task3_decor
def fibonacci(n):
    """ Calculation of n-th Fibonacci num """
    if n < 2: return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@task3_decor
def multiple_num(n):
    return n**3

print('Task 3')

A = [2, 1, 2, 5, 1, 5]
for n in A:
    print('{}! is {}'.format(n, factorial(n)))
    print('{}**3 is {}'.format(n, multiple_num(n)))