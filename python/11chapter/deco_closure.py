#!/usr/bin/env python

from time import time

def logged(when):
    def log(f, *args, **kargs):
        print '111111111111'
        print '''Called:
        function: %s
        args: %r
        kargs: %r''' % (f, args, kargs)

    def pre_logged(f):
        print '222222222222'
        def wrapper(*args, **kargs):
            print '33333333333'
            log(f, *args, **kargs)
            return f(*args, **kargs)
        return wrapper

    def post_logged(f):
        print '44444444444'
        def wrapper(*args, **kargs):
            print '5555555555'
            now = time()
            try:
                return f(*args, **kargs)
            finally:
                log(f, *args, **kargs)
                print "time delta:%s" % (time()-now)
        return wrapper

    try:
        print '66666666666'
        return {
        "pre": pre_logged,
        "post":post_logged}[when]
    except KeyError, e:
        raise ValueError(e), 'must be "pre" or "post"'

@logged("post")
def hello(name):
    print '77777777777'
    print "Hello", name

print '------------------------------------------------'
hello("World")
print '-----------------------------------------'
hello("python")
