# Функция range, генерирует список из количеста чисел переданных в значение функции range
# Функция range возвращает не настоящий список а утрируемые объекты диапозона и что бы
# превратить его в настощий список нужно передать это значение функции
# в функцию list эта конструкция позволяет получить нам массив/список из ста цифр
numbers = list(range(101))

print(numbers)

# Эта конструкция позволяет получить список/массив начиная с 50 до 101
numbers2 = list(range(50,101))

print(numbers2)

# Эта конструкция генерирует список/массив начиная с 0 до 101 с шагом 2
numbers3 = list(range(0,101,2))

print(numbers3)

# Сложный способ вывести список в столбик
numbers4 = [1,2,3,4,5]

i = 0
#переменная length получает количество объектов в списке,
# это 5 вычитает из них 1 и тем самым значение переменной
# length становиться 4
length = len(numbers4) - 1

print(length)

# Так как значение i=0 и соответственно оно меньше чем length который равен 4,
# на экран будет выведено значение первого объекта из списка number4, это 1
# Затем к i которая равна 0, будет прибавлено +1 и значение i станет 1
# на экран будет выведено значение второго объекта из списка number4, это 2 и т.д.
# пока i не станет меньше или равняться значению length который равен значению 4
# (четвертый индекс в списке равняется 5)
while i <= length:
    print(str(numbers4[i]) + ' !')
    i += 1

# Легкий способ вывести список в столбик (перебрать список)

for element in numbers4:
    print(str(element) + '  !')

# Выполняет код 15 раз
for test in range(15):
    print ('Привет')