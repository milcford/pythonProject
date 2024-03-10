n = int(input())
b = int(input())
p = 0
r = ''

while n >= b:
    p = n % b
    n //= b
    if p == 10:
        r += 'A'
        if n < b:
            r += str(n)
        continue
    if p == 12:
        r += 'C'
        if n < b:
            r += str(n)
        continue
    if p == 14:
        r += 'E'
        if n < b:
            r += str(n)
        continue
    r += str(p)
    if n < b:
        r += str(n)
print(r[::-1])
