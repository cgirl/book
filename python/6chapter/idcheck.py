#!/usr/bin/env python

import string

alphas = string.letters+'_'
nums = string.digits

print 'Welcome to the Identifier v1.0'
print 'test must be 2 chars long'
myInput = raw_input('Identified to test:')

flag = True
if len(myInput) > 1:
	if myInput[0] not in alphas:
		print '''invalid: first symbol must be in %s''' % alphas
	else:
		for eachChar in myInput[1:]:
			if eachChar not in alphas+nums:
				print '''invalid: remaining symbols must be chars or nums!'''
				flag = False
				break
		if flag:
			print "okay as an identifier!"
