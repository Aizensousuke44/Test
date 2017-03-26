from functools import reduce


def triple(x):
    return x ** 3

def normalize(name):
    return name[0].upper() + name[1:].lower()

# reduce(func, iterable_object)
# the func must have two arguments
def prod(L):
    return reduce(lambda x, y: x * y, L)

def multi(x, y):
    return x * 10 + y
def prod_second(L):
    return reduce(multi, L)

if __name__ == '__main__':
    result = map(triple, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(result))

    m = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(m))

    normal = ['aLlen', 'bOBY', 'CHRIs']
    n = list(map(normalize, normal))
    print(n)

    print(prod([3, 5, 7, 9]))
    print(prod_second([3, 5, 7, 9]))