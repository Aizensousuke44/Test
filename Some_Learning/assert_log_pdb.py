def division(m, n):
    n = int(n)

    assert n != 0, 'n is zero'
    print('n is not zero')
    return m/n

def logg(m, n):
    import logging
    logging.basicConfig(level=logging.INFO)
    num = int(n)
    logging.info('num = %d' % num)
    print(m/n)

#PDB

if __name__ == '__main__':
    result = division(0, 1)
    print(result)

    logg(50, 5)