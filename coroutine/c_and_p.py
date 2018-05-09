def consumer():
    r = ''
    s = ''
    while True:
        n = yield r, s
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'
        s = '200 YES'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r, s = c.send(n)
        print('[PRODUCER] Consumer return: %s...%s' % (r, s))
    c.close()


c = consumer()
produce(c)
