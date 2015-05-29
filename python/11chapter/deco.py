#!/usr/bin/env python
#coding:gbk

from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s called' % (ctime(), func.__name__)
        func()
        return func
    print 'the func is tsfunc'
    return wrappedFunc

print '----------------------'  #直接运行
@tsfunc                         #运行，返回wrappedFunc，即func也就是foo的引用,被包装为了wrappedFunc
def foo():
    print 'the func is foo'

print '*********************'   #直接运行

foo()                           #实际上是运行wrappedFunc
sleep(4)

for i in range(2):
    sleep(1)
    foo()
