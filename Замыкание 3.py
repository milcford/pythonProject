# Замыкание3

# Пример 1
'''
def everage_numbers():
    numbers = []
    def inner(number):
        numbers.append(number)
        print (numbers)
        return sum(numbers) / len(numbers)
    return inner

r1 = everage_numbers()

print(r1(5))
print(r1(10))
print(r1(13))

r2 = everage_numbers()

print(r2(100))
'''

# Пример 2
'''
def everage_numbers2():
    summa = 0
    count = 0

    def inner(number):
        nonlocal summa
        nonlocal count
        summa = summa + number
        count +=1
        return summa / count
    return inner

k = everage_numbers2()

print(k(10))
print(k(20))
print(k(30))
print(k(40))
'''

# Пример 3
'''
from datetime import datetime
from time import perf_counter

def timmer():
    start = perf_counter()
    def inner():
        return perf_counter() - start
    return inner

r = timmer()

print(r())
print(r())
'''

# Пример 4

def add(a,b):
    return a+b

def mult(a,b,c):
    return a*b*c

def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'функция {func.__name__} вызывалась {count} раз')
        return func(*args,**kwargs)
    return inner

s = counter(add)

print(s(2,4))
print(s(6,4))

m = counter(mult)

print(m(1,2,3))
print(m(1,2,4))


