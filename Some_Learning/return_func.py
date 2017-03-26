
def count():
    return lambda x: x ** 4

if __name__ == '__main__':
    res1 = count()
    print(res1(4))