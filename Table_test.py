s = input()
a = s.split()
# print(a)
s1 = ''

for i in range(len(a)):
    # print(a[i])
    for j in a[i]:
        # print(' ')
        if j.isalpha():
            s1 += j
            # print(j, end='')
    s1 += ' '
    # print('')
# print(s1)
s1 = s1.split()
# print(s1)
# print(len(s1[0]))


def encryption(s, shift):
    for i in s:
        if i.isalpha():
            if i == i.upper():
                if (ord(i) + shift) > 90:
                    print(chr((ord(i) + shift) - 26), end='')
                    continue
                else:
                    print(chr((ord(i) + shift)), end='')
                    continue
            if (ord(i) + shift) > 122:
                print(chr((ord(i) + shift) - 26), end='')
                continue
            else:
                print(chr((ord(i) + shift)), end='')
        else:
            print(i, end='')


for i in range(len(a)):
    encryption(a[i], len(s1[i]))
    print(' ', end='')

# Gdb, qmgi. "Ciev" ku b tpzahrl!
# Gdb, qmgi. "Ciev" ku b tpzahrl!