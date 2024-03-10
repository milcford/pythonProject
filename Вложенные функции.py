# Вложенные функции

g = 'gray'


def colors(param='r'):
    y = 'yellow'
    g = 'green'

    def red():
        r = 'red'
        print(r)

    def blue():
        b = 'blue'
        print(b)
    if param == 'r':
        red()
    elif param == 'b':
        blue()
    else:
        print('i dont know this color')


# red() Данную функцию можно вызывать только в локальной области функции colors()
colors('c')
