gender = {
    'm':'Дорогой',
    'f':'Дорогая'
}

a = [
    ['Семен', 'Семенович', 32.17, 'm'],
    ['Тамара', 'Ивановна', 123.12, 'f'],
    ['Михаил', 'Вячеславович', 1788.12, 'm']
]

for name,midname,balance,g in a:
    text = f'{gender[g]} {name} {midname}, баланс вашего лицевого счета составляет {balance} рублей'
    print(text)

d = []
for i in range(1,32):
    d.append(i)

print(len(d))
