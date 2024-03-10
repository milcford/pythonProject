# Генератор списка
a = [i**2 for i in range(1,7)]
print(a)

# Выражения генераторы
b = (i**2 for i in range(1,6))
print('first')
for i in b:
    print(i)

print('second')
for i in b:
    print(i)

b1 = (i ** 2 for i in range(1, 6))
print(sum(b1))

# c = (i for i in range(1000))
# for i in c:
#     print(i)