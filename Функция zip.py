a = [1, 2, 3, 4]

b = [100, 200, 300, 400]

for i in range(4):
    print(a[i], b[i])

rez = (zip(a, b))
# print(list(rez))

for i in rez:
    print(i, ' - обход циклом for')

print(rez)  # Объект zip является итерабельной последовательностью, ее можно обходить только 1н раз
print(list(rez), ' - вызов после обхода цикла for, список пуст так как объект zip уже обошли, в цикле for')

c = 'abcd'

rez2 = list(zip(a, b, c))  # Тут объект zip преобразован в список и можно уже сколько угодно раз его вызывать и обходить
print(rez2, ' - первый вызов')
print(rez2, ' - второй вызов')

for i in zip(a, b, c):
    print(i)

for t1, t2, t3 in zip(a, b, c):
    print(t1, t2, t3)

rez3 = zip(a, b, c)
col1, col2, col3 = zip(*rez3)

print(col1, col2, col3)
