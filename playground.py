def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(3, 4, 8, 34))


def calculate(**kwargs):
    print(kwargs)
    for keys, values in kwargs.items():
        print(keys)
        print(values)


calculate(add=4, multiply=6)
