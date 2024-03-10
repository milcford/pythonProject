print((lambda a, b: a * b)(17, 14))

def max(a, b):  # Наша функция проверяет какое число больше
    if a > b:
        return a
    else:
        return b
print(max(25, 17))

print((lambda a, b: a if a > b else b)(25, 17)) # все тоже самое что и функция max

# Домашнее задание
print((lambda a: a * 4)(5)) # Тут мы вычисляем периметр квадрата
print((lambda a, b, c: (a + b + c)/3)(15,20,25)) # Тут мы вычисляем среднее значение из трех чисел
