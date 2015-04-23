#!/usr/bin/env python

db = {}

def newuser():
    prompt = 'login desired:'
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'name token, try another!'
            continue
        else:
            break
    pwd = raw_input('passwd:')
    db[name] = pwd

def olduser():
    name = raw_input('login:')
    pwd = raw_input('passwd:')
    passwd = db.get(name)
    if passwd == pwd:
        print 'welcome back', name
    else:
        print 'name or passwd error'

def showmenu():
    prompt = '''
(N)ew user login
(E)xisting user login
(Q)uit

Enter your choice:'''
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nyour picked:[%s]' % choice
            if choice not in 'neq':
                print 'invalid choice, try again'
            else:
                chosen = True
                
        if choice == 'q':
            done = True
        if choice == 'n':
            newuser()
            print 'new user input suceess!'
        if choice == 'e':
            olduser()

if __name__ == '__main__':
    showmenu()
                

