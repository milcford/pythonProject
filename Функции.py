def sayhello():
    print('Hello')
    print('World')
    print('and everybody')


sayhello()


def square(x):
    print('Квадрат числа', x, '=', x ** 2)


square(5)
square(10)

for i in range(1, 11):
    square(i)


def multyplay(x, y):
    print(x * y)


multyplay(2, 5)


def even(a):
    if a % 2 == 0:
        print(a, 'четное')
    else:
        print(a, 'нечетное')


for i in range(20):
    even(i)


def factorial(n):
    pr = 1
    for i in range(2, n + 1):
        pr = pr * i
    print(pr)


factorial(5)

if 5 > 6:
    def primer():
        print('hello')
else:
    def primer():
        print('HELLO')

primer()