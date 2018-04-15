f = None
try:
    f = open('aaaa', 'r')
except FileNotFoundError as ioe:
    print('ファイルが見つかりませんでした')
finally:
    if f:
        f.close()
