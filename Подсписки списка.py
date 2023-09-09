s = input().split()
print(len(s))

l1 = []
for i in range(len(s) - 0):
    l1.append([s[i + 0]])
print(l1)

# l2 = []
for i in range(len(s) - 1):
    l1.append([s[i],s[i + 1]])
print(l1)

# l3 = []
for i in range(len(s) - 2):
    l1.append([s[i],s[i + 1],s[i + 2]])
print(l1)

# l4 = []
for i in range(len(s) - 3):
    l1.append([s[i],s[i + 1],s[i + 2],s[i + 3]])
print(l1)

# l5 = []
for i in range(len(s) - 4):
    l1.append([s[i],s[i + 1],s[i + 2],s[i + 3],s[i + 4]])
print(l1)




