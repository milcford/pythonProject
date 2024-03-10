d = {}
d['a'] = 1
print(d)
if 'a' in d:
    d['a'] += 1
else:
    d['d'] = 1
print(d)

if 'b' in d:
    d['b'] += 1
else:
    d['b'] = 1
print(d)

# s = input()
s = 'фыва ффывафывафыва3465346(;.;,.,.;,98.,:%№"№%'
d1 = {}
for i in s:
    if i.isalpha():  # Проверка на буквы, если i является буковй
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
print(d1)

# Функция sorted сортирует наш словарь по алфавиту
for i in sorted(d1):
    print(i, d1[i])

d2 = {}
for i in s:
    if i.isalpha(): # Проверка на буквы, если i является буковй
        d2[i] = d2.get(i,0) + 1
for i in sorted(d2):
    print(i, d2[i])
print(d2)


# words = {}
# while True:
#     s1 = input()
#     if s1 in words:
#         print('Слово',s1, 'переводится как', words[s1])
#     else:
#         print('Введите перевод слова ',s1)
#         words[s1] = input()

contacts = {
    'Марат Хайруллин': {
        'birthday': '19 april 1988', 'city':'Sochi',
        'phone':'79284579121','children':'1'
    },
    'Аня Леденева': {
        'birthday': '12 февраля 1987', 'city': 'Sochi',
        'phone': '79628863525', 'children': '1'
    }
}


persons = (['Марат Хайруллин', 'Аня Леденева'])
# for person in persons:
#     birthday = contacts[person]['birthday']
#     city = contacts[person]['city']
#     phone = contacts[person]['phone']
#     children = contacts[person]['children']
#     print(person,children, phone)

for person in persons:
    print(person)
    for data in contacts[person]:
        print(data, contacts[person][data])
