# Работа с модулями

# Импортируем модуль random
import random

# randint это функция которая находится в модуле random
# И в данном случае она представлена как метод
print(random.randint(1,100))

# Выводит на экран 10 рандомных значений
for x in range(10):
    print(random.randint(1,100))



# Позволяет импортировать определенную функцию/метод из модуля random
from random import randint

# Можно сразу указывать медот модуля, т.к. она определенным образом импортированна
print(randint(1,100))



# Позволяет импортировать все медоты из модуля random
from random import *

# Можно сразу указывать метод модуля, т.к. все методы/функции модуля random импортированны
print(randint(1,100))


# Импортировали медот sqrt который позволяет возвращать корень числа
from math import sqrt
print (sqrt(16))

# Импортировать все медоты из модуля random
from math import *
print(pi)

# Импортирует два метода указанных через запятую
from math import sqrt, pi
print(pi)

# Импортируем функцию sqrt и переименовывем ее для нашего кода
from math import sqrt as my_sqrt