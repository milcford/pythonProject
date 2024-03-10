a = [0, 0, 5, 4, 2, 3, 4, 5, 4, 3, 2, 5]
count = [0] * 6
for i in a:
    count[i] += 1
print(count)
for i in range(6):
    if count[i] > 0:
        print(i, 'встретился', count[i], 'раз', end=' ')
        # print((str(i) + ' ') * count[i], end='')
