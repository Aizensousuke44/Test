
def _not_division(n):
    return lambda x: x % n > 0

def odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def prime():
    n = 2
    oi = odd_iter()
    while True:
        n = next(oi)
        yield n
        # UNSOLVED
        oi = filter(_not_division(n), oi)

if __name__ == '__main__':
    for n in prime():
        if n < 20:
            print(n)
        else:
            break
