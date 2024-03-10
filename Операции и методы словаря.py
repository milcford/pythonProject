a = [['Moskva', 495], ['Piter', 812], ['Penza', 8412]]

d = {
    'moskva': 495,
    'piter': 812,
    'penza': 8412
}
print(d, ' - простой словарь')

# Создание словаря с помощью метода dict
r = dict(moskva=495, piter=812, penza=8412)
print(r, ' - словарь созданный с помощью присвоения значения ключам')

t = dict(a)
print(t, ' - словарь сеозданный из вложенных списков')

# Метод fromkeys создает ключи для словаря
q = dict.fromkeys(['a', 'b', 'c'])
print(q, ' - Созданный словарь с применением метода fromkeys без указания значений')

q1 = dict.fromkeys(['a', 'b', 'c'], 100)
print(q1, ' - каждому ключу присвоенно одно и тоже значение')

v = {}
v1 = dict()
print(v, type(v))
print(v1, type(v1))

d1 = {
    1: 'one',
    2: 'two',
    3: 'three',
}

d1[4] = 'four'  # Добавляет в словарь новый ключ со значением
d1[5] = 'пять'

print(d1)
d1[3] = 'Три'
print(d1)
print(d1[1])
print(d1[4])

person = {}
s = 'MARAT KHAIRULLIN SOCHI RUDN 5 4 5 3 3 3 3 4 5'
s = s.split()
person['firstName'] = s[0]
person['lastName'] = s[1]
person['city'] = s[2]
person['univer'] = s[3]
person['marks'] = []
for i in s[4:]:
    person['marks'].append(int(i))
print(s)
print(person)

d3 = {
    1: 'one',
    2: 'two',
    3: 'three'
}

print(d3)
del d3[3]
print(d3)
print(1 in d3, 5 in d3, 7 not in d3)
print(len(d3))
if 5 in d3:
    print(d3[5])
else:
    d3[5] = 'five'
print(d3)

for key in d3:
    print(key, d3[key])

d3.clear()  # Очищает полностью словарь
print(d3)

d4 = {
    1: 'one',
    2: 'two',
    3: 'three'
}

print(d4.get(1), ' - получаем значение ключа 1')
print(d4.get(4))  # значение None
print(d4.get(4, 'такого ключа нет'))
print(d4.get(6, [1, 2, 3]))

# Метод setdefault: если в словаре есть ключ, тогда ничего не произойдет
# Если в словаре нет ключа тогда он будет добавлен с переданным ему значением
d4.setdefault(2,'два')
d4.setdefault(6,'шесть')
print(d4)

# Метод pop выводит значение по ключу, а сам ключ и значение удаляет из списка
print(d4.pop(2))
print(d4)

if 2 in d4:
    d4.pop(2)
    print(d4)
else:
    d4[2] = 'ДВА'
    print(d4)

# Метод popitem удаляет случайную пару ключ:значение
d4.popitem()
print(d4)
d4.popitem()
print(d4)

print(d4.keys(), ' - выводит на экран все ключи из словаря')
print(d4.values(), ' - выводит на экран все значения из словаря')

for key in d4.keys():
    print(key, d4[key])

for value in d4.values():
    print(value)

# Метод items возвращает нам коллекцию содержащую все пары ключ - значения
print(d4.items())

for item in d4.items():
    print(item, ' - содержимое представляет собой кортеж')

for item in d4.items():
    print(item[0], ' - выводит ключ')

for key,value in d4.items():
    print(key,value, ' - выводится и ключ и значение')


