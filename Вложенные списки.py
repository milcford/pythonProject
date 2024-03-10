# a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, [4, 5, 7, 11], 17, 19]]
#
# print(len(a))
# print(a[2])
# print(a[2][3])
# print(a[0][1])
# print(a[2][2][1])

# b = ['hello', 'hi', 'world']
#
# print(b[2])
# print(b[2][0])
# print(b[2][-1])

# a = [
#     [0, 2, 4, 6],
#     [1, 5, 9, 13],
#     [3, 10, 17, 19]
# ]

# for i in a:
#     print(i)

# for i in a:
#     for j in i:
#         print(j, end=' ')
#     print()

# for i in range(3):
#     for j in range(4):
#         print(a[i][j], end=' ')
#     print()

# for i in range(3):
#     s=0
#     for j in range(4):
#         s+=a[i][j]
#     print(s) # сумма построчно
# print()
#
# for j in range(4):
#     s=0
#     for i in range(3):
#         s+=a[i][j]
#     print(s) # сумма по столбцам

a = []
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))

# создаем список потом выводим его несколько раз
for i in range(n):
    a.append([0] * m)
for i in a:
    print(i)
