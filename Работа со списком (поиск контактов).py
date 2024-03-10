contacts = {
    "Марат" : "+79284579121",
    "Аня" : "+79628863525",
    "Мама" : "+79183019320"
}

testing = input("Кого ищем? ")

if testing in contacts:
    print('Контакт найден: ' + contacts[testing])
else:
    print('Контакт не найден')