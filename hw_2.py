#1)Дан массив из словарей 
data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]
#1.1) отсортировать массив из словарей по значению ключа ‘age' 

def sort_age(dictionary):
    return dictionary['age']

data.sort(key=sort_age)
#print(data)

#1.2) сгруппировать данные по значению ключа 'city' 
# вывод должен быть такого вида :

# def sort_city(dictionary):
#     return dictionary['city']
# data.sort(key=sort_city)

result = {}
for elem in data:
    if elem['city'] not in result.keys():
        result[elem['city']]=[]
    result[elem.pop('city')].append(elem)
print('1)', result)

# result = {
#    'Kiev': [{'name': 'Viktor', 'age': 30 },
#              {'name': 'Andrey', 'age': 34}],
#    'Dnepr': [{'name': 'Maksim', 'age': 20 },
#               {'name': 'Artem', 'age': 50}],
#    'Lviv': [{'name': 'Vladimir', 'age': 32 },
#              {'name': 'Dmitriy', 'age': 21}]
# }
# =======================================================
# 2) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:

def most_frequent(list_var):
    n = 0
    mf = []
    for elem in list_var:
        num = list_var.count(elem)
        if num > n:
            n = num
            mf = [elem]
        elif num == n and elem not in mf:
            mf.append(elem)
    return mf

print('2)', most_frequent(['a', 'a', 'bi', 'bi', 'bi']))

# =======================================================
# 3) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.

def multipl_dig(integer_num):
    st_num = str(integer_num).replace('0','')
    if len(st_num) == 0:
        res = 0
    else:
        res = 1
        for elem in st_num:
            res *= int(elem)
    return res

print('3)', multipl_dig(12300987))

# =======================================================
# 4) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.

def hw2_func(array, exp):
    if exp >= len(array):
        return -1
    else:
        return array[exp]**exp

print('4)', hw2_func([2, 3, 2, 4, 6.22, 3.14], 6))

# =======================================================
# 5) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.

def three_words(spec_string):
    n_words = 0
    p = spec_string.find(' ')
    while n_words < 3 and p != -1:
        if '1234567890'.find(spec_string[p+1]) != -1:
            n_words = 0
        else:
            n_words += 1
        p = spec_string.find(' ', p+1)
    if n_words == 3:
        return ('There are three words in a row: ' + spec_string)
    else:
        return ('There are not three words in a row: ' + spec_string)

print('5)', three_words("hello 1 one two three 15 world"))