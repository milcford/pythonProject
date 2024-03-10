# Работа с файлами

'''
#  Открываем файл в режиме чтения, выводим содержимое файла на экран,
#  закрываем файл (что бы не занимал место в оперативной памяти).

file = open('/Users/milcford/PycharmProjects/pythonProject/venv/text.txt', 'r')

print(file.read(6))  # в скобках указывается кол-во байт, которые надо прочитать из файла
print(file.read(3))  # во второй раз он выведет кол-во байтов после первого вывода

file.close()
'''

'''
#  Спрашиваем у пользователя, какой файл надо открыть
filename = input('Укажите файл: ')
file = open(filename, 'r')

print(file.read())

file.close()


# Считаем сколько символов у нас в файле
filename = input('Укажите файл: ')
file = open(filename, 'r')

print('В данном файле ' + str(len(file.read())) + ' символов.')

file.close()

# Если файл что-то содержит, тогда он будет перезаписан под ноль
file = open('/Users/milcford/PycharmProjects/pythonProject/venv/test2.txt', 'w')
file.close()


# Если такого файла не существует, он будет создан
file = open('/Users/milcford/PycharmProjects/pythonProject/venv/test3.txt', 'w')
file.close()
'''

'''
# Записываем в файл данные 
file = open('/Users/milcford/PycharmProjects/pythonProject/venv/test3.txt', 'w')
file.write('Привет МиР!')
file.close()
'''

'''
# Создание файла через запрос у пользователя
filename = input('Введите имя файла: ')
text = input('Какой текст хотите поместить в файл? ')

file = open(filename, 'w')

file.write(text)

file.close()
'''

'''
# Добавляем данные в файл с помощью метода appeend используя ключ a
file = open('/Users/milcford/PycharmProjects/pythonProject/venv/test.txt', 'a')

file.write(' TEST')

file.close()
'''

file = open('/Users/milcford/PycharmProjects/pythonProject/venv/test.txt', 'r')
for i in range(21):
    print(file.read(6))

file.close()