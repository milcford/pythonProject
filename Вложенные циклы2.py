from string import printable

# for b1 in printable:
#     for b2 in printable:
#         for b3 in printable:
#             print(b1,b2,b3)

# k = 0
# for b1 in range(1, 5):
#     for b2 in range(1, 5):
#         for b3 in range(1, 5):
#             for b4 in range(1, 5):
#                 print(b1, b2, b3, b4)
#                 k += 1
# print(k, 'комбинаций пароля из цифр 1 2 3 4')

# for i in range(1, 10):
#     for j in range(1, 11):
#         print(i, '*', j, '=', i * j, end=' ')
#     print()
# print()
#
# for j in range(1, 10):
#     for i in range(1, 11):
#         print(i, '*', j, '=', i * j, end=' ')
#     print()

# k = 0
# for b1 in 'tukva':
#     for b2 in 'tukva':
#         for b3 in 'tukva':
#             for b4 in 'tukva':
#                 for b5 in 'tukva':
#                     for b6 in 'tukva':
#                         word = b1 + b2 + b3 + b4 + b5 + b6
#                         if word[0] in 'tkv' and word[-1] in 'tkv':
#                             if word.count('a') + word.count('u') == 2:
#                                 # print(word)
#                                 k += 1
# print(k)

for i in range(1, 10001):
    x = i
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    print(i, s)
