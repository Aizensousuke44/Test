# __str__ print()
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name=%s)' % self.name

    # __repr__ = __str__

# __iter__
class Fibo(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    # generator
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

# __getitem__ & slice
class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 0, 1
            for i in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            end = item.stop
            if start is None:
                start = 0
            a, b = 0, 1
            L = []
            for i in range(end):
                if i > start:
                    L.append(a)
                a, b = b, a + b
            return L

# __getattr__ call the property not exist in class
# call __getattr__
class School(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == 'addr':
            return 'CN.Shenzhen'
        raise AttributeError('School object has no attribute %s' % item)


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s-%s' % (self._path, item))

    def __str__(self):
        return self._path


if __name__ == '__main__':
    '''__str__'''
    s = Student('Joker')
    print(s)
    print(Student('Batman'))

    '''__iter__'''
    f = Fibo()
    for i in f:
        print(i)

    '''__getitem__'''
    f = Fib()
    print(f[10])
    print(f[4:10])

    '''__getattr__'''
    s = School('Akon')
    print(s.name)
    print(s.addr)
    # print(s.area)

    create_ = Chain()
    print(create_.a.b.c.d.e.f)
    print(create_.list)

    '''__call__'''
    print(callable(Chain))