import random

a = []
for i in range(10):
    a.append(random.randint(-10, 10))

count = [0] * 21
for i in a:
    count[i+10] += 1
print(a)

for i in range(21):
    if count[i] > 0:
        print(i-10,count[i])
