#try:
#    pogoda = 'Плохая'
#    if pogoda == 'Плохая':
#        raise TypeError # создаем собственное исключение с помощью команды raise
#except TypeError:
#    print('Поймано исключение TypeError')


#pogoda = 'Плохая'
#if pogoda == 'Плохая':
#     raise TypeError('Описание ошибки') # в скобках добавили описание для созданного исключения


#try:
#    pogoda = 'Плохая'
#    if pogoda == 'Плохая':
#        raise TypeError
#except:
#    print('Исключение поймано') # мы ловим свое созданное исключение

#try:
#    print (7/0)
#except:
#    print('Тест')
#    raise

class milcfordError(Exception): # создаем свой тип исключений
    pass
raise milcfordError('Тест')