#!/usr/bin/env python
import types

def displayNumType(num):
	print num, 'is',
	if isinstance(num, (str, int, long, float, complex)):
		print 'a number of type:%s' % type(num).__name__
	else:
		print 'not a num of all!!'

displayNumType(-69)
displayNumType(99999999999999999999999999999L)
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('xxxx')

print '-------------------------------------------------'
def displayNumType1(num):
	print num, "is",
	if type(num) == type(0):
		print 'a integer'
	elif type(num) == type(0L):
		print 'a long'
	elif type(num) == type(0.00):
		print 'a float'
	elif type(num) == type(0+0j):
		print 'a complex number!'
	else:
		print ' not a number at all!!'

displayNumType1(-69)
displayNumType1(99999999999999999999999999999L)
displayNumType1(98.6)
displayNumType1(-5.2+1.9j)
displayNumType1('xxxx')
	
print '-------------------------------------------------'
def displayNumType2(num):
	print num, "is",
	if type(num) is types.IntType:
		print 'a integer'
	elif type(num) is types.LongType:
		print 'a long'
	elif type(num) is types.FloatType:
		print 'a float'
	elif type(num) is types.ComplexType:
		print 'a complex number!'
	else:
		print ' not a number at all!!'

displayNumType2(-69)
displayNumType2(99999999999999999999999999999L)
displayNumType2(98.6)
displayNumType2(-5.2+1.9j)
displayNumType2('xxxx')
print '-------------------------------------------------'
from types import IntType
from types import LongType
from types import FloatType
from types import ComplexType
def displayNumType3(num):
	print num, "is",
	if type(num) is IntType:
		print 'a integer'
	elif type(num) is LongType:
		print 'a long'
	elif type(num) is FloatType:
		print 'a float'
	elif type(num) is ComplexType:
		print 'a complex number!'
	else:
		print ' not a number at all!!'

displayNumType3(-69)
displayNumType3(99999999999999999999999999999L)
displayNumType3(98.6)
displayNumType3(-5.2+1.9j)
displayNumType3('xxxx')
