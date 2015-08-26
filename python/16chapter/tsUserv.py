#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

updSerSock = socket(AF_INET, SOCK_DGRAM)
updSerSock.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = updSerSock.recvfrom(BUFSIZ)
    updSerSock.sendto('[%s] %s' % (ctime(), data), addr )
    print '...received from and returned to:', addr

upSerSock.close()
