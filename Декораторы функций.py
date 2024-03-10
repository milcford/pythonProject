# Создаем функцию декоратор, которая будет получать в качестве
# аргумента нашу функцию которую декоратор будет оборачивать
def my_decor(func):
    # Внутри декоратора мы создает вложеннцю функцию-обертку
    # которая будет работать непосредственно с полученной функцией
    # на входе наш декоратор
    def wrapper():
        # Внутри нее мы вызовем нашу переданную функцию
        print('start')
        func()
        print('end')
    # Функция-декоратор вернет как значение функцию "wrapper"
    return wrapper

def my_func():
    print('Тут основная функция')

# Первый вариант (обычный способ декорирования функции)
# Создадим переменную my и присвоим ей значение выполнения функции-декоратора
# и ей передаем как значение нашу функцию my_func
my = my_decor(my_func)
# После чего вызываем переменную my как функцию
my()

# Второй вариант с более удобным написанием кода
def my_decor2(func):
    def wrapper():
        print('Начало выполнения функции')
        func()
        print('Конец выполнения функции')
    return wrapper

@my_decor2
def my_func():
    print('Тут основная функция')

my_func()

# Пример использования декоратора
def my_decor3(func):
    def wrapper(n):
        print('Старт')
        func(n)
        print('Конец')
    return wrapper

@my_decor3
def my_func(number):
    print(number ** 2)

my_func(10)

@my_decor3
def my_func(number):
    print(number ** 3)

my_func(100)

import time
# Создаем декоратор который будет замерять время выполнения переданных ему функций
def my_decor4(func):
    def my_wr():
        start_time = time.time()
        func()
        print(time.time() - start_time, 'столько времени потребовалось для выполнения функции')
    return my_wr

@my_decor4
def sp():
    list = [i ** 2 for i in range(1000000) if i % 2 == 0]
    print(list)

sp()


