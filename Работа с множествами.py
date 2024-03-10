numbers = {1, 5, 6, 78, 98, 5, 4}
print(numbers)
print(type(numbers))

numbers2 = set() # Создаем пустое множество
print(type(numbers2))

numbers3 = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8]
set_numbers3 = set(numbers3) # Преобразовываем Список в Множество
# print(set_numbers3)
list_set_numbers3 = list(set_numbers3) # Преобразовываем Множество в Список
# print(list_set_numbers3)

set_numbers3.add(58) # Добавляем в наше множество элемент 58

set_numbers3.discard(59) # Удаляем элемент из множества, если данного элемента нет ошибки не будет.

set_numbers3.remove(58) # Удаляем элемент из множества, если данного элемента нет будет ошибка.

set_numbers3.pop() # Удалем первый элемент из множества
print(set_numbers3, 'Выводит множество set_numbers3, после применения метода set_numbers3.pop() ')

# set_numbers3.clear() # Полностью очищает множества от Элементов
# print(set_numbers3, 'Выводит множество set_numbers3, после применения метода set_numbers3.clear()')

print(list_set_numbers3, 'Выводит преобразованный список из множества')

#union_numbers = numbers.union(set_numbers3) # Объеденяем два множества
union_numbers = numbers | set_numbers3 # Объеденяем два множества
print(union_numbers, '- объединенные множества с помощью метода union')

# intersection_numbers = numbers.intersection(set_numbers3) # Выводит только те элекменты которые есть в обоих множествах
intersection_numbers = numbers & set_numbers3 # Выводит только те элекменты которые есть в обоих множествах
print(intersection_numbers, '- результат применения метода numbers.intersection(set_numbers3)')

numbers4 = numbers - set_numbers3 # Выводит на экран элементы множества
# numbers отличные от элементов множества set_numbers3
print(numbers4, '- множество numbers4')

copy_numbers = numbers.copy() # Копирует элементы из одного множества в другой
print(numbers, '- множество numbers')
print(copy_numbers, '- множество copy_numbers')
print(len(numbers), '- количество элементов numbers')

numbers = frozenset(numbers) # Замороженное множество, которое нельзя изменять 
print(numbers, '- замороженное множество numbers')

# for i in set_numbers3:
#     print(i)

print(3 in set_numbers3)
print(58 in set_numbers3)