# Форматирование строк, метод format

name = 'Marat'
age = 34

person_name = 'Marat'
person_age = 34

print('Привет, %s!\nТебе уже %d год!' % (name, age))

# %s - Плейсхолдер строки
# %d - Плейсхолдер числа
# %f - Плейсхолдер дроби


print('Привет, {}\nТебе уже {} года!'.format(name,age) )

print( '{0}{1}{0}'.format('abra','cad') )

print('Привет, {name}\nТебе уже {age} года!'.format( name = person_name, age = person_age ) )


person = {
    'name' : 'Marat',
    'age' : 21
}

print ( 'Имя: {name}\nВозраст: {age}'.format( name = person['name'], age=person['age']  ) )


human = {
    'name' : 'Marat',
    'age' : 21
}

print ( 'Имя: {person[name]}\nВозраст: {person[age]}'.format( person = human ) )


input_str = 'Марат'

print( '{0:*^11}'.format(input_str) )
print( '{0:*<11}'.format(input_str) )
print( '{0: >11}'.format(input_str) )
print( '{0:>11}'.format(input_str) )


# Таким способом можно отцентровать наше значение
input_str = 'Marat'
lenght = 15

if (len(input_str) % 2):
    lenght +=1 # Тоже самое что lenght = lenght + 1

print (( '{0:*^' + str(lenght) + '}' ).format (input_str))
