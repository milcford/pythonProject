a = [2 for i in range(10)]
print(a)

a = [i for i in range(10)]
print(a)

a = [i ** 2 for i in range(10)]
print(a)

a = [i % 4 for i in range(1, 15)]
print(a)

a = [i % 4 for i in range(1, 15)]
print(a)

a = [i for i in 'hello']
print(a)

a = [i * 5 for i in 'hello']
print(a)

# Функция ord находит код символа в таблице ASCII
a = [ord(i) for i in 'hello']
print(a)

a = [ord(i) for i in 'abcd']
print(a)

import random

a = [random.randint(-10, 10) for i in range(10)]
print(a)

b = [abs(elem) for elem in a]
print(b)

a = [elem + 1 for elem in a]
print(a)

a = [elem * 3 for elem in a]
print(a)

b = [elem for elem in a if elem % 2 == 0 and elem % 3 == 0]
print(b)
