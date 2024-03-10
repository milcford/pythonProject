# Декораторы2

# Передача информации о функции в декоратор

# Способ 1
'''
def table(func):

    def inner(*args,**kwargs):
        print('<table>')
        func(*args,**kwargs)
        print('</table>')
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner

def say():
    print('Hello world')

def sqr(x):
    """
    Функция возводит x в квадрат
    :param x:
    :return:
    """
    print(x**2)

sqr = table(sqr)

sqr(2)

print(sqr.__name__)
print(sqr.__doc__)
'''


# Способ 2

from functools import wraps
def table(func):

    @wraps(func)              # Передает информацию о декорируемой функции
    def inner(*args,**kwargs):
        print('<table>')
        func(*args,**kwargs)
        print('</table>')
    return inner

def say():
    print('Hello world')

def sqr(x):
    '''
    Функция возводит x в квадрат
    :param x:
    :return:
    '''
    print(x**2)

sqr = table(sqr)

sqr(5)

print(sqr.__name__)
print(sqr.__doc__)

import math