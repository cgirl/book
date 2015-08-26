#!/usr/bin/env python

stack = []

def pushit():
    stack.append(raw_input('Enter the string:').strip())

def popit():
    if len(stack) == 0:
        print 'no data!'
    else:
        print 'Remove [', stack.pop(), ']'

def viewstack():
    print stack

CMDs = {'u':pushit, 'o':popit,  'v':viewstack}

def showmenu():
    pr = '''
p(U)sh
p(O)p
(V)iew
(Q)uit

Enter choice:
'''
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexEorror):
                choice = 'q'
            print '\nyour picked:[%s]' % choice
            if choice not in 'ouvq':
                print 'invoild option, try again'
            else:
                break
        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()
