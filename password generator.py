import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
ambiguous_chars = 'il1Lo0O'

chars = ''

counts_password = input('Количество паролей для генерации?: ')
lenght_password = input('Длинна пароля?: ')
choice_digits = input('Включать ли цифры 0123456789? д/н: ')
choice_uppercase_letters = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? д/н: ')
choice_lowercase_letters = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? д/н: ')
choice_punctuation = input('Включать ли символы !#$%&*+-=?@^_?: ')
exclude_chars = input('Исключать ли неоднозначные символы il1Lo0O? д/н: ')

if choice_digits == 'д':
    chars += digits
if choice_uppercase_letters == 'д':
    chars += uppercase_letters
if choice_lowercase_letters == 'д':
    chars += lowercase_letters
if choice_punctuation == 'д':
    chars += punctuation
if exclude_chars == 'д':
    for i in ambiguous_chars:
        chars = chars.replace(i, '')

def generate_password(length, chars):
    password = random.sample(chars, int(length))
    return password

for i in range(int(counts_password)):
    print(''.join(generate_password(lenght_password,chars)))
