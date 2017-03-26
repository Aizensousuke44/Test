import hashlib

db = {}

def get_md5(salt):
    md5 = hashlib.md5()
    md5.update(salt.encode('utf8'))
    return md5.hexdigest()

def register(username, passwd):
    db[username] = get_md5(passwd + username + 'the-salt')

def login(username, passwd):
    if username in db:
        if db[username] == get_md5(passwd + username + 'the-salt'):
            return True
    return False

def status_(bl):
    if bl:
        print('Welcome')
    else:
        print('Password is not correct')


if __name__ == '__main__':

    ''' MD5 '''

    md5 = hashlib.md5()
    md5.update('How to use md5 in python hashlib?'.encode('utf8'))
    print(md5.hexdigest())
    md5.update('How to use md5 in python hashlib?'.encode('utf8'))
    print(md5.hexdigest())

    ''' SHA1 '''

    sha1 = hashlib.sha1()
    sha1.update('How to use sha1 in python hashlib?'.encode('utf8'))
    print(sha1.hexdigest())


    register('aizen', 'aizen44')
    status_(login('aizen', 'aizen44'))