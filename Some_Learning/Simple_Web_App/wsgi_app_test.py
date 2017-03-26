
def application(env, stat_reponse):
    stat_reponse('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello World</h1>' % (env['PATH_INFO'][1:])
    return [body.encode('utf8')]