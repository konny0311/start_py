def nabe(a):
    if int(a) % 3 == 0 or '3' in a:
        return 'アホ'
    return a

a = input('数字を入力してください')
result = nabe(a)
print(result)
