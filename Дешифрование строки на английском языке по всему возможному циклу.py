s = input('Текст для шифрования/дешифрования: ')

for shift in range(-25, 0):
    for i in s:
        if i.isalpha():
            if i == i.upper():
                if (ord(i) + shift) < 65:
                    print(chr((ord(i) + shift) + 26), end='')
                    continue
                else:
                    print(chr((ord(i) + shift)), end='')
                    continue
            if (ord(i) + shift) < 97:
                print(chr((ord(i) + shift) + 26), end='')
                continue
            else:
                print(chr((ord(i) + shift)), end='')
        else:
            print(i, end='')
    print('')