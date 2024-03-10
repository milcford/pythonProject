encryption = input('1 - шифрование, 2 - дешифрование ?: ')
language = input('1 - English, 2 - Русский: 1/2 ?: ')
shift = int(input('Введите сдвиг шифра: '))
s = input('Текст для шифрования/дешифрования: ')  # To be, or not to be, that is the question!
a = []

if encryption == '1': # ШИФРОВАНИЕ
    if language == '1': # ENGLISH
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

    if language == '2': # RUSSIAN
        for i in s:
            if i.isalpha():
                if i == i.upper(): # Для заглавных букв мы используем другой диапазон кодового значения букв, т.к. они отличаются от строчных.
                    if (ord(i) + shift) > 1071:
                        print(chr((ord(i) + shift) - 32), end='')
                        continue
                    else:
                        print(chr((ord(i) + shift)), end='')
                        continue
                if (ord(i) + shift) > 1103:
                    print(chr((ord(i) + shift) - 32), end='')
                    continue
                else:
                    print(chr((ord(i) + shift)), end='')
            else:
                print(i, end='')

if encryption == '2': # ДЕШИФРОВАНИЕ
    shift = shift * -1
    if language == '1': # ENGLISH
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
                    print(chr((ord(i) + shift) +26), end='')
                    continue
                else:
                    print(chr((ord(i) + shift)), end='')
            else:
                print(i, end='')

    if language == '2': # RUSSIAN
        for i in s:
            if i.isalpha():
                if i == i.upper():
                    if (ord(i) + shift) < 1040:
                        print(chr((ord(i) + shift) + 32), end='')
                        continue
                    else:
                        print(chr((ord(i) + shift)), end='')
                        continue
                if (ord(i) + shift) < 1072:
                    print(chr((ord(i) + shift) + 32), end='')
                    continue
                else:
                    print(chr((ord(i) + shift)), end='')
            else:
                print(i, end='')

# Умом Россию не понять.
# Фнпн Спттйя ож рпоауэ.
# Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.
# Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.
# Скупой терЯет все, желаЯ все достатЬ.

# Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.
