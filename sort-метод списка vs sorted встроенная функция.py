# sort-метод списка vs sorted встроенная функция

a = [4, -10, 43, -300, 500, 54, 89, -34]
b = 'hello world'
c = ('hi', 'zero', 'abracadabra', 'picachu')

# a.sort() # Применяется только к списку
# b.sort() # Ошибка, даже синтаксис подсвечивается как ошибка
# c.sort()

# a.sort()
sorted(a)  # sorted в отличии от sort не изменяет начальную коллекцию
print(sorted(a), ' - выводится отсортированный список')
print(a, ' - изначальный список не поменялся')
a = sorted(a) # В случае присвоения изначальный список будет изменен
print(a, ' - тут выводится изменные список после присвоения переменной')

b = sorted(b)
print(b)

c = sorted(c)
print(c)

c = sorted(c, reverse=True)
print(c)

c = sorted(c, reverse=False)
print(c)

b = sorted(b, reverse=True)
print(b)

b = sorted(b, reverse=False)
print(b)

a = sorted(a, reverse=True)
print(a)

a = sorted(a, reverse=False)
print(a)

