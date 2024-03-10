# Метод lower

input_str = input('Введите что угодно:')
print(input_str.lower())

name = input('Введите ваше имя:')

if( name.lower().startswith('м')):
    print('Добро пожаловать\nВы находитесь в элитном клубе людей, имена которых начинаются с буквы "М"! ')
else:
    print('Добро пожаловать!')

name2 = input('Введите ваше имя на любом языке:')

if( name2.lower().startswith('м') or name2.lower().startswith('m') ):
    print('Добро пожаловать\nВы находитесь в элитном клубе людей, имена которых начинаются с буквы "М"! ')
else:
    print('Добро пожаловать!')