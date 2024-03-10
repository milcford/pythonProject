a = [4, 10, 43, -300, 54, 289, -34, -8, 749]

print(sorted(a, key=abs))  # Список выводится как есть, но сортируется по модулю числа

a = [4, 10, 43, 300, 54, 289, 34, 8, 749]


def f(x):
    return x % 10


print(
    sorted(a, key=f))  # Список отсортирован по ключу key в который передана наша функция, сортировка по последнему чилу


def f(x):
    return -(x % 10)


print(sorted(a, key=f))


def f(x):
    return x % 10, x // 10 % 10


print(sorted(a,
             key=f))  # В первую очередь происходит сортировка по последний цифре, если последние цифры равны тогда идет сортировка по второй цифре

a = ['ZZZ', 'aaa', 'eee', 'DDD', 'BBB', 'www']
print(sorted(a))

a = ['ZZZ', 'aaa', 'eee', 'DDD', 'BBB', 'www']
print(sorted(a, key=str.lower))

a = ['ZZZ 79', 'aaa 45', 'eee 43', 'DDD 800', 'BBB 5', 'www 14']
print(sorted(a, key=lambda x: int(x.split()[1])))

a = ['ZZZ 800', 'aaa 45', 'eee 43', 'DDD 800', 'BBB 43', 'www 14']
print(sorted(a, key=lambda x: (int(x.split()[1]), x.split()[0])))

a = ['ZZZ 800', 'aaa 45', 'eee 43', 'ddd 800', 'BBB 43', 'www 14']
print(sorted(a, key=lambda x: (int(x.split()[1]), x.split()[0].lower()), reverse=True))

a = ['ZZZ 800', 'aaa 45', 'eee 43', 'ddd 800', 'BBB 43', 'www 14']
print(sorted(a, key=lambda x: (x.split()[0].lower(), int(x.split()[1]) )))

a = ['ZZZ 800', 'aaa 45', 'eee 43', 'ddd 800', 'AaA 43', 'aaa 14']
print(sorted(a, key=lambda x: (x.split()[0].lower(), int(x.split()[1]) )))

a = ['ZZZ 800', 'aaa 45', 'eee 43', 'ddd 800', 'AaA 43', 'aaa 14']
a = sorted(a, key=lambda x: int(x.split()[1]) )

a = sorted(a, key= lambda x: x.split()[0].lower(), reverse=True)
print(a)

a = ['ZZZ 800', 'aaa 45', 'eee 43', 'ddd 800', 'AaA 43', 'aaa 14']
a = sorted(a, key=lambda x: -int(x.split()[1]) )

a = sorted(a, key= lambda x: x.split()[0].lower(), reverse=True)
print(a)