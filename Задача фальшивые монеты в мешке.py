import random

bag1 = [5,5,5,5,5]
bag2 = [5,5,5,5,5]
bag5 = [5,5,5,5,5]
bag4 = [5,5,5,5,5]
bag3 = [4,4,4,4,4]
bags = [bag1, bag2, bag3, bag4, bag5]

r = random.randint(1,5)
bag_total = []

for i in range(1,6):
    bag_total.append(bags[i - 1][:i])

count = 0
for i in bag_total:
    count += sum(i)

print(bag_total)
print(count)

print(f'Фальшивые монеты в {75 - count} мешке')


