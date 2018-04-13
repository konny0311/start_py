num = 1
array = []
while num < 11:
    array.append(num)
    num += 1

for v in array:
    if v % 2 == 1:
        print(v)
    else:
        print("偶数")
