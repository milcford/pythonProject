import re

s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'
result = re.match('AC', s) # метод match ищет подстрочку AC с начала строки
print(result, '- показывает что подстрочка AC найдена и выводит индекс строки в котором она найдена')

result = re.match('DC', s) # метод match ищет подстрочку DC с начала строки
print(result, '- так как строчка не начинается с DC')

result = re.search('DC', s) # метод search ищет подстрочку DC по всей строке s
print(result, '- отображает первое найденное упоминание в строчке и выводит индекс строки в которой ')

result = re.search('DC', s) # метод search ищет подстрочку DC по всей строке s
print(result[0], '- отображает искомую подстроку ')

result = re.findall('DC', s) # метод findall ищет все подстрочки и формирует из найденных элементов список
print(result, '- отображает все найденные элементы в виде списка ')

result = re.split('/', s) # метод split делит нашу строку по указонному элементу "/"
print(result, '- отображает разделенные элементы в виде списка ')

result = re.split('/', s, maxsplit=2) # метод split, аргумент maxsplit указывает кол-во разбитий которое надо применить к строке
print(result, '- отображает разделенные элементы в виде списка, с применением аргумента maxsplit')

result = re.sub('A', 'D', s) # метод sub производит замену символа A на символ D
print(result, '- отображает строку после применения метода sub ')

result = re.fullmatch('A', s) # метод fullmatch проверяет равняется ли символ A строке s
print(result, '- так как символ A не является/равняется строке s ')

sa = 'A'
result = re.fullmatch('A', sa) # метод fullmatch проверяет равняется ли символ A строке sa
print(result, '- строка является полностью одинаковой строке sa и отображается индекс')

