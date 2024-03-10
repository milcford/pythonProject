# for i in range(3):
#     for j in range(5):
#         print('*', end='')
#     print()

for i in range(3):
    for j in range(5):
        print(i, end='')
    print()
print()

for i in range(3):
    for j in range(5):
        print(j, end='')
    print()
print()

for i in range(10):
    for j in range(i):
        print(j, end='')
    print()
print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, end='')
    print()
print()

for i in range(1, 4):
    for j in range(10, 13):
        print(i, j)
