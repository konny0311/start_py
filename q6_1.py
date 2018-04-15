def test(idx):
    abc = ['a', 'b', 'c']
    try:
        print(abc[idx])
    except IndexError as ie:
        print('指定するインデックス番号は存在しません。')

idx = int(input('数字を入力してください。'))
test(idx)
