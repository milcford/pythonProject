try: # попытаться выполнить команду
    print(7/0)
except ZeroDivisionError: # ловим ошибку деление на 0
    print ('Поймано исключение ДелениеПоНулю ') # если поймана нужная ошибка выполнится данный код
print('Программа завершена')

try:
    print(7/0)
except ZeroDivisionError:
    pass # если поймана нужная ошибка, просто пропускаем ее и код выполняется дальше
print('ПРОГРАММА  завершена')

try:
    print(7/0)
except: # ловит все ошибки
    print ('Поймано исключение ')
print('Программа завершена')


try:
    print(name/0)
except ZeroDivisionError:
    print('Поймано исключение ДелениеПоНулю ')
except NameError:
    print('Поймана исключение НеСуществующаяПеременная ')
except:
    print ('Поймано исключение ')
print('Программа завершена')


try:
    print(name/0)
except (ZeroDivisionError, NameError, TypeError, ValueError): # ловим перечесленные исключения
    print('Поймано плохое исключение ')
print('Программа завершена')


try:
    print(7/0)
except (ZeroDivisionError, NameError, TypeError, ValueError):
    print('Поймано плохое исключение ')
finally: # исполняет код в независимости было поймано исключение или не было
    print('Конец поимки')
print('Программа завершена')

