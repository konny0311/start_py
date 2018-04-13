import random

def random_array(size):
    array = []
    for v in range(size):
        array.append(random.randint(0,100))
    return array

result = random_array(10)
print(result)
