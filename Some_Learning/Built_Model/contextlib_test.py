from contextlib import contextmanager


class Query(object):

    def __init__(self, name):
        self.name = name
    # create class-object by with as
    # first run __enter__
    def __enter__(self):
        print('Open to Begin')
        return self
    # finish statements in with as, and run __exit__
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('Finished')

    def query(self):
            print('Query info about %s' % self.name)


''' Contextlib '''

class Query_(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s' % self.name)

# yield to be a generator
@contextmanager
def create_query(name):
    print('Begin')
    q = Query_(name)
    yield q
    print('End')

@contextmanager
def tag(tg):
    print('<%s>' % tg)
    yield
    print('</%s>' % tg)


if __name__ == '__main__':

    with Query('Joker') as jk:
        jk.query()

    print()
    print('Contextlib')
    with create_query('Joker') as jk:
        jk.query()

    with tag('html'):
        with tag('body'):
            print('Joker')
            print('Main page')

    ''' closing
        closing can change the object not context to be context in with as
    '''

    from contextlib import closing
    from urllib.request import urlopen

    with closing(urlopen('https://www.python.org')) as page:
        for line in page:
            print(line)