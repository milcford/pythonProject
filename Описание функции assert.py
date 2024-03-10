# assert - утверждение (используется для предположения чего либо)

def exc(text):
    assert text != '' # text не равно пусто
    print(str(text + '!')) # Если текст не равен пустоте, то выполняется данный код

#exc('')

def test(number):
    assert number > 0, 'Введено число меньше 0' # number больше нуля, то выполнится код ниже
    print(str(number))

test(-1)