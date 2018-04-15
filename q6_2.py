def add_number(a, b):
    try:
        return a + b
    except TypeError as te:
        print('数字を入力してください')

add_number(1, 'b')
