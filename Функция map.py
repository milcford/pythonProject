a = [-3, -2, -1, 0, 1, 2, 3]

# Функция map
b = [abs(-3), abs(-2), abs(-1), abs(0), abs(1), abs(2), abs(3)]
b1 = list(map(abs, a))
b2 = [abs(i) for i in a]

print(b)
print(b1)
print(b2)


# Функция map может принимать самописные функции
def f(x):
    return x ** 2


b3 = list(map(f, a))

print(b3)

a1 = ['hello', 'hi', 'good morning']
b4 = list(map(len, a1))
print(b4)
b5 = list(map(str.upper, a1))
print(b5)
b6 = list(map(lambda x: x[::-1], a1))
print(b6)
b7 = list(map(lambda x: x+'!', a1))
print(b7)
b8 = list(map(list, a1))
print(b8)
c = list(map(sorted, b8))
print(c)

s = list(map(int, input('Введите числа: ').split()))
print(s)