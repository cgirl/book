#!/usr/bin/env python

queue = []

def enQ():
    queue.append(raw_input('Enter date:').strip())

def deQ():
    if len(queue) == 0:
        print 'no data'
    else:
        print 'Remove [', queue.pop(), ']'

def ViewQ():
    print queue

CMDs = {'u':enQ, 'o':deQ, 'v':ViewQ}

def showmenu():
    pr = '''
Enter your choice:
p(U)sh
p(O)p
(V)iew
(Q)uit

Enter choice:'''

    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except(EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'
        
            print 'your picked:[%s]' % choice
            if choice not in 'qvuo':
                print 'involid choice, try again'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
   showmenu() 
