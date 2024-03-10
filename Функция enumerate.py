a = [10, 20, 30, 40, 50, 60]
s = 'hello'
t = ('apple','banan','mango')
d = {'a':1,'b':2,'c':3}

# print(list(enumerate(a)))
#
# for para in enumerate(a):
#     print(para)
#
for index,value in enumerate(t,10):
    print(index,value)

# for index, value in enumerate(a):
#     if value % 20 == 0:
#         print(index, value)
#
# for index, value in enumerate(a):
#     a[index]+=1
