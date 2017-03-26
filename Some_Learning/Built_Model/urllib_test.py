from urllib import parse, request

def with_GET(path):

    # for browser
    req = request.Request(path)
    req.add_header('User-Agent', 'Mozilla...')

    with request.urlopen(req) as dd:
        data = dd.read()
        print('Status: %s, %s' % (dd.status, dd.reason))

        for key, value in dd.getheaders():
            print('%s: %s' %(key, value))
        print('Data: ', data.decode('utf8'))


def with_POST(path):
    print('Login in some website')
    username = input('Username: ')
    passwd = input('Password: ')
    login_data = parse.urlencode(
        [
            ('username', username),
            ('password', passwd),
            ('entry', 'website_name'),
            ('client_id', ''),
            ('savestate', '1'),
            ('ec', ''),
            ('pagerefer', 'https://...')
        ]
    )

    req = request.Request(path)
    req.add_header('User-Agent', 'Mozilla...')
    req.add_header('Referer', 'https://...')

    with request.urlopen(req, data=login_data.encode('utf8')) as req_post:
        print('Status: ', req_post.status, req_post.reason)
        for key, value in req_post.getheaders():
            print('%s: %s' % (key, value))

        print('Data: ', req_post.read().decode('utf8'))

if __name__ == '__main__':
    path = 'https://api.douban.com/v2/book/2129650'
    with_GET(path)

    # with_POST(path)