'''# Программа для копирования файлов

filename1 = input('Введите имя копируемого файла: ')
filename2 = input('Введите, куда скопировать файл?: ')

file1 = open(filename1, 'r')
file2 = open(filename2, 'w')

file2.write(file1.read())

file1.close()
file2.close()

print('Копирование успешно завершено !')
'''

'''
# Тут я создал файл в корне папки, что бы его можно было забэкапить
file = open('/Users/milcford/PycharmProjects/pythonProject/venv/milcford.txt', 'w')
file.close()
'''

'''
# Спрашиваем какой файл нам забэкапить 
filename1 = input('Какой файл забэкапить?: ')
filename2 =  'backup_' + filename1

file1 = open(filename1, 'r')
file2 = open(filename2, 'w')

file2.write(file1.read())

file1.close()
file2.close()

print('Бэкап прошел успешно!')
'''

# Копируем бинарные файлы, содержащие мультимеа данные
filename1 = input('Какой файл забэкапить?: ')
filename2 =  'backup_' + filename1

file1 = open(filename1, 'rb')
file2 = open(filename2, 'wb')

file2.write(file1.read())

file1.close()
file2.close()

print('Бэкап прошел успешно!')