#!/usr/bin/env python
# -*- coding:gbk -*-

def deco(func):
    def _deco():
        print '\nbefore myfunc() called.'
        func()
        print 'alfter myfunc() called.'
        return func
    return _deco

@deco
def myfunc():
    print ' myfunc() called.'
    return 'ok'

#myfunc = deco(myfunc)

myfunc()
myfunc()
