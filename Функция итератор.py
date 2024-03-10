# def f():
#     return [45, 345, 23]
#
#
# print(f())
#
#
# def genf():
#     for i in [45, 345, 23]:
#         yield i
#
#
# # yield возвращает значение и замораживает вашу функцию со всеми локальными переменнами на этом месте
#
# s = genf()
# print(next(s))
# print(next(s))
# print(next(s))
#
# for i in genf():
#     print(i)


def f1():
    s = 7
    for i in [45, 345, 23]:
        yield i
        print(s)
        s = s * 10 + 7

g = f1()
print(next(g), 'тут выведено значение 45')
print(next(g), 'тут выведено значение 345, а строчкой выше выведено значение s')
print(next(g))
