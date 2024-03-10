def f(x):
    if x > 10:
        return True
    else:
        return False


def f1(x):
    return x > 9 and x < 100


a = [14, 0, 5, 79, 645, 7952, 10, 0, 192, 471]
b = list(filter(f1, a))
b1 = [i for i in a if i > 9 and i < 100]
print(b)
print(b1)

a1 = [14, 0, ' ', [5], 'hello', [], '', 79, 645, 7952, 10, 0, 192, 471]
b2 = list(filter(bool, a1))
print(b2)
b3 = list(filter(None, a1))
print(b3)

a2 = ['word', 'hello', '234', 'potato', 'hi']
b4 = list(filter(lambda x: len(x) > 5, a2))
print(b4)

a3 = '4asdfMNB76786VJHVjhbmnbmtrtr7576'
b5 = list(filter(str.isdigit, a3))
print(b5)
b6 = list(filter(str.isalpha, a3))
print(b6)
b7 = list(filter(str.isupper, a3))
print(b7)

d = {
    'moscow': 800,
    'boston': 750,
    'LA': 400,
    'SF': 900,
    'Chicago': 650,
    'SP': 600,
}

b8 = list(filter(lambda x: d[x] > 700, d))
print(b8)

b9 = list(filter(lambda x: len(x) > 3, d))
print(b9)
