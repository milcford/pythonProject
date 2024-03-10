
'''
# Выводит на экран данные из файла в одну строку
file = open('milcford.txt', 'r')

strings = file.readlines()

print(strings)

file.close()
'''


'''
# Выводит данные построчно
file = open('milcford.txt', 'r')

strings = file.readlines()

for string in strings:
    print(string )


file.close()
'''

# С помощью команды with можно открыть файлы передавая их
# в свою переменную, файл после этого закрывать не надо

with open('milcford.txt', 'r') as milc:
    print(milc.read(5))

print(milc.read())
