def f(x):
    return x ** 2


r = lambda x: x ** 2

print(r(7))


def perimetr(a, b, c):
    return a + b + c


per = lambda a, b, c: a + b + c
print(per(3, 5, 7))

h = lambda: 'hello'

print(h())


def f2(x):
    if x > 0:
        return 'positive'
    else:
        return 'negative'


t = lambda x: 'positive' if x > 0 else 'negative'

print(t(0))

a = [78, 56, 23, 8, 54512, 65, 95, 2354, 41, 5000]
a.sort()
print(a)


def f(x):
    return x % 10


# a.sort(key=f)
a.sort(key=lambda x: x // 10 % 10)
print(a)


def linear(k, b):
    return lambda x: x * k + b

graf1 = linear(2,5)
print(graf1(3))

graf2 = linear(-4,1)
print(graf2(5))
