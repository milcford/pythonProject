# n = input()
n = '110101'
# base_number = int(input())
base_number = 2

lenght = len(n)
count = lenght - 1
total_count = 0
d = 0

for i in range(lenght):
    if n[i] == 'A':
        d = 10 * base_number ** count
        count -= 1
        total_count += d
        continue
    if n[i] == 'F':
        d = 15 * base_number ** count
        count -= 1
        total_count += d
        continue
    d = int(n[i]) * base_number ** count
    count -= 1
    total_count += d
print(total_count)
