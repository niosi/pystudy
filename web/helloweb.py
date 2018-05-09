def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    ew = environ['PATH_INFO'][1:] or 'web'
    print(ew)
    body = '<h1>Hello, %s!</h1>' % (ew)
    return [body.encode('utf-8')]