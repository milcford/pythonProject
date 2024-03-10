def rec0(s):
    if len(s) == 1 or len(s) == 2:
        return s
    return s[0] + '(' + rec0(s[1:-1]) + ')' + s[-1]


s = "любое слово"
print(rec0(s))

a = [1, 2, [2, 3, 4, [3, 4, [2, 3], 5]]]


def rec(spisok, level=1):
    print(*spisok)
    for i in spisok:
        print(i, type(i))


rec(a)


def rec1(spisok, level=1):
    print(*spisok,'level=',level)
    for i in spisok:
        if type(i) == list:
            rec1(i, level + 1)


rec1(a)
