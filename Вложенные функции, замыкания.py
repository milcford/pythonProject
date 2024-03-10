def degree(x):
    y = 2
    def degree_two():
        return y ** x
    return degree_two()

print(degree(4))

def message(number):
    def print_message():
        return 'Число ' + str(number)
    return print_message()
print(message(78))
print(print_message) # Нашу вложенную функцию не видно, так как она скрыта за нашей функцией