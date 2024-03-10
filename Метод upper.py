# Метод upper

input_str = input('Введите что угодно:')
print(input_str.upper())

name = input('Введите ваше имя:')

if( name.upper().startswith('М')):
    print('Добро пожаловать\nВы находитесь в элитном клубе людей, имена которых начинаются с буквы "М"! ')
else:
    print('Добро пожаловать!')

name2 = input('Введите ваше имя на любом языке:')

if( name2.upper().startswith('М') or name2.upper().startswith('M') ):
    print('Добро пожаловать\nВы находитесь в элитном клубе людей, имена которых начинаются с буквы "М"! ')
else:
    print('Добро пожаловать!')