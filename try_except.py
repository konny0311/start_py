try:
    file = open('a.txt', 'r')
except FileNotFoundError as fne:
    print('そのファイルは存在しません。')
