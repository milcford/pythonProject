def summa(*args): # Сперва идет * потом любое название, принимает любое количество аргументов
    print(args) # выводит в виде кортежа

summa(1,4,6,76,75,45,4,89)

def brand(**brands): # Сперва идет ** потом любое значение, принимает именные аргументы
    print(brands)
    for x, y in brands.items():
        print(x, ':', y)

brand(a = 'Apple', s =' Samsung')