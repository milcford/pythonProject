#
# a = [
# ('Sidorov', 1995),
# ('Lukov', 2002),
# ('Petrov', 1991),
# ('Gorbachev', 1984),
# ('Kostin', 2000),
# ('Isaev', 2005),
# ('Eliseev', 1999),
# ('Kozlov', 2004),
# ('Bukov', 1995),
# ('Gavrilov', 1980),
# ('Efremov', 2006),
# ]
#
# b = [elem[0] for elem in a]
# print(b)
# b = [elem[1] for elem in a]
# print(b)
#
# b = [elem[0] for elem in a if elem[0].startswith('E')]
# print(b)
#
# b = [elem[0][0] for elem in a if elem[1] > 2000]
# print(b)

# a = {
#     'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
#     'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
#     'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
#     'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
#     'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
#     'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
#     'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
#     'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
#     'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'}
# }
#
# b = [(elem,a[elem]['hobby']) for elem in a if a[elem]['age'] < 2000 and a[elem]['hobby']=='soccer']
# print(b)
#
#
# s = 'askdjfhalksdjfalkjso8798asdf87a6sdf875as78dfa98sdfu'
# s1 = [int(i) for i in s if i.isdigit()]
# print(s1)
#
# s1 = [i for i in s if i.isalpha()]
# print(s1)

import random

n = 7
m = 7

# a = [[random.randint(1,6) for j in range(m)] for i in range(n)]
# for i in a:
#     print(i)
# b = [a[i][j] for i in range(n) for j in range(m) if i==j]
# print('main diagon', b)
# c = [a[2][j] for j in range(m)]
# d = [a[i][3] for i in range(n)]
# print('2 str', c)
# print('4 stolb', d)

a = [ [i*j for j in range(1,m+1)] for i in range(1,n+1)]
for i in a:
    print(i)
