a = (1, 2, 3, 4, 5, 5, [1, 2, 3, 4, 5])  # Кортеж
a1 = 6, 7, 8  # Это тоже кортеж

print(a, type(a))
print(a1, type(a1))
b = tuple(range(5))  # Создаем кортеж
print(b, type(b))
c = ()
print(c, type(c))

print(len(a))
print(len(a1))
print(5 in a, 6 in a, 6 not in a)
# print(a + a1, a1 + a)
# print(a * 2)
# print(min(a), max(a1))
# print(sum(a))
print(a.count(5))  # Считает сколько раз встречается объект в кортеже
print(a.index(2))  # Отображает индекс объекта
print(a[-1]) # Сам кортеж не изменяемый объект
a[-1].append(100) # Но список внутри кортежа является изменяемым объектом
print(a[-1])

b1 = [1,2,3,4,5,6,'hi', 'hello']
b2 = tuple(b1) # Кортеж занимает меньше памяти чем список

print(b1.__sizeof__()) # Выводит размер в байтах
print(b2.__sizeof__()) # Выводит размер в байтах
