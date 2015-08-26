#!/usr/bin/env python

'''
An example of reading and writing Unicode strings:Writes a Unicode string to a file in utf-8,and read itback in.
'''

CODEC = 'utf-8'
FILE  = 'unicode.txt'

hello_out = u'Hello World!\n'
byte_out  = hello_out.encode(CODEC)

f = open( FILE, 'w' )
#f.write(byte_out)
f.write(hello_out)
f.close()

f = open( FILE, 'r' )
byte_in = f.read()
f.close()
print byte_in,
hello_in = byte_in.decode(CODEC)
print hello_in,
