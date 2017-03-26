from functools import wraps

# when the program finished
# test.__name__ will changed to wrapper
# if no wraps(func)
def log(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('%s: %s()' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log('Call')
def test():
    print('Hello')

''' args '''

def demo(args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('%s: %s()' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper

    if isinstance(args, str):
        text = args
        return decorator
    else:
        text = 'execute'
        return decorator(args)

@demo
def test1():
    print('The args is exist or not')

@demo('Hello')
def test2():
    print('The args is exist or not')

if __name__ == '__main__':
    test()
    print(test.__name__)

    test1()
    print(test1.__name__)

    test2()
    print(test2.__name__)