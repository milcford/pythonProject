s = input().split()
print(s)
print(len(s))

l1 = []

for i in range(len(s) - 0):
    l1.append(s[i:i + 1])
print(l1)

for i in range(len(s) - 1):
    l1.append(s[i:i + 2])
print(l1)


for i in range(len(s) - 2):
    l1.append(s[i:i + 3])
print(l1)


for i in range(len(s) - 3):
    l1.append(s[i:i + 4])
print(l1)

for i in range(len(s) - 4):
    l1.append(s[i:i + 5])
print(l1)
