#!/usr/bin/env python
'readFileText.py -- read and display text file'

#get file name
fname = raw_input('Enter your filename:')

#attemp to open your file to reading
try:
	fobj = open(fname, 'r')
except IOError, e:
	print "*** file open error:", e
else:
	#display contents to screen
	for eachLine in fobj:
		print eachLine,
	fobj.close()

