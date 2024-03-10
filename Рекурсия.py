# def rec(x):
#     print(x)
#     rec(x+1)
#
# rec(1)

def fact(x):
    if x == 1:
        return 1
    return fact(x - 1) * x


print(fact(4))
print(fact(10))


def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(10))


def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0 ] != s[-1]:
        return False
    return palindrom(s[1:-1])

print(palindrom('шалаш'))
