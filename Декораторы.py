# Декораторы
# Декоратор это функция которая принимает другую функцию и возвращает функцию,
# декораторы нужны для того что бы в вашей функции добавилось новое поведение или новый функционал

# Пример 1
'''
def decorator(func):

    def inner():
        print('start decorator')
        func()
        print('finish decorator')

    return inner

def say():
    print('Hello world')

def bay():
    print('Bay world')

# d = decorator(say)
# d()

say = decorator(say)
say()

bay = decorator(bay)
bay()
'''

# Пример 2
'''
def decorator(func):

    def inner(*args,**kwargs):
        print('start decorator')
        func(*args,**kwargs)
        print('finish decorator')

    return inner

def say(name, surname, age ):
    print('Hello', name, surname, age)

say = decorator(say)
say('Vasya', 'Ivanov', 34)
'''

# Пример 3

def header(func):

    def inner(*args,**kwargs):
        print('<h1>')
        func(*args,**kwargs)
        print('</h1>')

    return inner

def table(func):

    def inner(*args,**kwargs):
        print('<table>')
        func(*args,**kwargs)
        print('</table>')

    return inner

def say(name, surname, age ):
    print('Hello', name, surname, age)

# say = table(header(say))
# say('Vasya', 'Ivanov', 34)

say = header(table(say))
say('Vasya', 'Ivanov', 34)

@header # say = header(say)
def say(name, surname, age ):
    print('Hello', name, surname, age)

say('Vasya', 'Ivanov', 34)


@table # say = table(say)
def say(name, surname, age ):
    print('Hello', name, surname, age)

say('Vasya', 'Ivanov', 34)

@header
@table # say = header(table(say))
def say(name, surname, age ):
    print('Hello', name, surname, age)

say('Vasya', 'Ivanov', 34)





