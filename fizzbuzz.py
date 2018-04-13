num = input("数字入力お願いします")
num = int(num)
if num % 15 == 0:
    print('fizzbuzz')
elif num % 5 == 0:
    print('fizz')
elif num % 3 == 0:
    print('buzz')
else:
    print(num)

num += 1
