n = 10

first = 0
second = 1

temp = 0
# 0 1  1 2 3 5 8 13
print(first,second,end = " ")
for i in range(2,n):
    temp = second + first
    print(temp, end = " ")
    first = second
    second = temp
print(temp)