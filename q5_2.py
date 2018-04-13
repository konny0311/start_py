def get_sum(**kargs):
    sum = 0
    for v in range(int(kargs["start"]), int(kargs["end"]+1)):
        sum += v
    print(sum)

get_sum(start=1, end=10)
