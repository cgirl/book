#!/usr/bin/env python

class NumStr(object):
    def __init__(self, num=0, string=''):
        self.num = num
        self.string = string

    def __str__(self):
        return '[%d::%r]' % (self.num, self.string)

    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other, NumStr):
            return self.__class__(self.num+other.num, self.string+other.string)
        else:
            raise TypeError,\
                'Illegal argument type for built-in operation'
    
    def __mul__(self, num):
        if isinstance(num, int):
            return self.__class__(self.num*num, self.string*num)
        else:
            raise TypeError,\
                'Illegal argument type for built-in operation'

    def __nozero__(self):
        return self.__num or len(self.__string)

    def __norm_cval(self, cmpres):
        return cmp(cmpres, 0)

    def __cmp__(self, other):
        return self.__norm_cval(cmp(self.num, other.num))+self.__norm_cval(cmp(self.string, other.string))

a = NumStr(3, 'foo')
print a
b = NumStr(3, 'goo')
print b
c = NumStr(2, 'foo')
print c
d = NumStr()
print d
e = NumStr(string = 'boo')
print e
f = NumStr(1)
print f

if d:
    'd not false'
if e:
    'e bot false'
mm = cmp(a, b)
print 'a,b %d' % mm
print 'a,c %d' % cmp(a, c)
print 'a,a %d' % cmp(a, a)

print 'a+b =',
print a+b
print 'c*5 =',
print c*5
