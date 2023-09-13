from functools import reduce
from my_calc import *
import time


# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.


def square(x):
    tpl_square = (x * 4, x * x, (2 ** 0.5) * x)
    return tpl_square


#     return f'''Периметр квадрата = {x * 4}
# Площадь квадрата = {x * x}
# Диагональ квадрата = {(2 ** 0.5) * x}'''


a = square(5)
print(a)
print('-----------------------')


# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

def display(**kwargs):
    for key, value in kwargs.items():
        print(key, ':', value)


display(name='John', last_name='Smith', age=35, position='web developer')
print('-----------------------')

# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
my_list = [20, -3, 15, 2, -1, -21]
my_new_list = list(filter(lambda x: x > 0, my_list))
print(my_new_list)
print('-----------------------')

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
reduced_result = reduce(lambda x, y: x * y, my_new_list)
print(reduced_result)
print('-----------------------')


# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
def decorated_function(func):
    def wrapper(*args):
        start_time = time.time()
        print('Start time: ', start_time)
        print(func(*args))
        end_time = time.time()
        print('End time: ', end_time)
        elapsed_time = end_time - start_time
        print('Elapsed time: ', elapsed_time)

    return wrapper


@decorated_function
def hello(item):
    return f'I\'m a wrapped function, {item} is wrapped'


def decorated_function_2(func):
    def wrapper(**kwargs):
        start_time = time.time()
        print('Start time: ', start_time)
        print(func(**kwargs))
        end_time = time.time()
        print('End time: ', end_time)
        elapsed_time = end_time - start_time
        print('Elapsed time: ', elapsed_time)

    return wrapper


@decorated_function_2
def display_it(**kwargs):
    for key, value in kwargs.items():
        print(key, ':', value)


def decorated_function_3(func):
    def wrapper(*args):
        start_t = time.time()
        print('Start wrapper at: ', start_t)
        print(func(*args))
        end_t = time.time()
        print('End wrapper at: ', end_t)
        print('Used time for running function: ', start_t - end_t)

    return wrapper


@decorated_function_3
def using_wrapper_func(*args):
    return sum(args)


display_it(name='John', last_name='Smith', age=35, position='web developer')
print('-----------------------')

hello('Suuuper')
print('-----------------------')

using_wrapper_func(4, 5, 88)
print('-----------------------')

# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
print(summa(4, 5))
print(minus(4, 5))
print(mnozym(4, 5))
print(delym(4, 5))
