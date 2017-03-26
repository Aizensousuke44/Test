
def test(self, name='Hacker'):
    print('Hello, %s' % name)

Hello = type('Hello', (object,), dict(hello=test))


''' metaclass'''
class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaClass):
    pass


if __name__ == '__main__':
    h = Hello()
    print(type(h))
    print(type(Hello))
    print(h.hello('Joker'))

    l = MyList()
    l.add(7)
    print(l)