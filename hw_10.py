# Задача-1
# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерировании по генератору необходимо проверять строки на уникальность.
# Если строка уникальна, тогда ее выводим на экран, если нет - скипаем


def unique_lines_in_file(f_name):
    unique = set()
    with open(f_name, 'r') as f:
        for line in f:
            n_line = line.strip()
            if n_line not in unique:
                unique.add(n_line)
                yield n_line


unique_lines = unique_lines_in_file("g.txt")

for line in unique_lines:
    print(line)

# Задача-2 (оригинальный вариант и его делать не обязательно):
# представим есть файл с логами, его нужно бессконечно контролировать
# на предмет возникнования заданных сигнатур.
#
# Необходимо реализовать пайплайн из корутин, который подключается к существующему файлу
# по принципу команды tail, переключается в самый конец файла и с этого момента начинает следить
# за его наполнением, и в случае возникнования запиcей, сигнатуры которых мы отслеживаем -
# печатать результат
#
# Архитектура пайплайна

#                    --------
#                   /- grep -\
# dispenser(file) <- - grep - -> pprint
#                   \- grep -/
#                    --------

# Структура пайплайна:
# ```

import time


def coroutine(func):
    def wrapper(*args, **kwargs):
        cor = func(*args, **kwargs)
        next(cor)
        return cor
    return wrapper


@coroutine
def grep(pattern, target_func):
    while True:
        line = yield
        if pattern in line:
            target_func.send(line)


@coroutine
def printer():
    while True:
        line = yield
        print(line)


@coroutine
def dispenser(list_of_greps):
    while True:
        line = yield
        for arg in list_of_greps:
            arg.send(line)


def follow(opened_file, target):
    opened_file.seek(0, 2)
    while True:
        line = opened_file.readline()
        if not line:
            time.sleep(1)
            continue
        target.send(line)

# ```
#
# Каждый grep следит за определенной сигнатурой
#
# Как это будет работать:
#
# ```

f_open = open('log.txt')  # подключаемся к файлу

follow(f_open,
       # делегируем ивенты
       dispenser([
           grep('python', printer()),  # отслеживаем
           grep('is', printer()),      # заданные
           grep('great', printer()),   # сигнатуры
       ])
       )
# ```
# Как только в файл запишется что-то содержащее ('python', 'is', 'great') мы сможем это увидеть
#
# Итоговая реализация фактически будет асинхронным ивент хендлером, с отсутствием блокирующих операций.
#
# Если все плохо - план Б лекция Дэвида Бизли
# [warning] решение там тоже есть :)
# https://www.dabeaz.com/coroutines/Coroutines.pdf


#Задача-3 (упрощенный вариант делаете его если задача 2 показалась сложной)
# Вам нужно создать pipeline (конвеер, подобие pipeline в unix https://en.wikipedia.org/wiki/Pipeline_(Unix)).
#
# Схема пайплайна :
# source ---send()--->coroutine1------send()---->coroutine2----send()------>sink
#
# Все что вам нужно сделать это выводить сообщение о том что было получено на каждом шаге и обработку ошибки GeneratorExit.
#
# Например: Ваш source (это не корутина, не генератор и прочее, это просто функция ) в ней опеделите цикл из 10 элементов
# которые будут по цепочке отправлены в каждый из корутин и в каждом из корутив вызвано сообщение о полученном элементе.
# После вызова .close() вы должны в каждом из корутин вывести сообщение что работа завершена.