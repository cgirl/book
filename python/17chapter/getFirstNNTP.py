#!/usr/bin/env python
#-*- coding:utf-8 -*-

import nntplib
import socket

#HOST = 'blog.sina.com.cn'
HOST = 'web.aioe.org'
GRNM = 'comp.lang.python'
USER = 'wesley'
PASS = "you'llNerverGuess"

def main():
    #连接新闻服务器
    try:
        n = nntplib.NNTP(HOST)
    except socket.gaierror, e:
        print 'ERROR: cannot reach host "%s"' % HOST
        print '("%s")' % str(e)
        return
    except nntplib.NNTPPermanentError, e:
        print 'ERROR: access denied on "%s"' % HOST
        print '("%s")' % str(e)
        return
    print '*** Connect to host "%s"' % HOST
    
    try:
        rsp, ct, fst, lst, grp = n.group(GRNM)
    except nntplib.NNTPTemporaryError, e:
        print 'ERROR: cannot load group "%s"' % GRNM
        print '(%s)' % str(e)
        print 'Server may require authentication'
        print 'Uncomment/edit login line above'
        n.quit()
        return
    except nntplib.NNTPTemporaryError, e:
        print 'ERROR: group "%s" unavailable' % GRNM
        print '(%s)' % str(e)
        n.quit()
        return
    print '*** Found newsgroups "%s"' % GRNM

    rng = '%s-%s' %(lst, lst)
    rsp, frm = n.xhdr('from', rng)
    rsp, sub = n.xhdr('subject', rng)
    rsp, dat = n.xhdr('date', rng)
    print '''*** Found last article(#%s):

    From: %s
    Subject: %s
    Date: %s
    ''' % (lst, frm[0][1], sub[0][1], dat[0][1])

    rsp, anum, mid, data = n.body(lst)
    displayFirst20(data)
    n.quit()

def displayFirst20(data):
    print '*** First (<=20) meaningful lines:\n'
    count = 0
    lines = (line.strip() for line in data)
    lastBlank = True
    for line in lines:
        if line:
            lower = line.lower()
        if(lower.startswith('>') and not lower.startswith('>>>')) or \
            lower.startswith('|') or lower.startswith('in article') or \
            lower.endswith('writes:') or lower.endswith('wrote:'):
            continue
        if not lastBlank or (lastBlank and line):
            print '%s' % line
        if line:
            count += 1
            lastBlank = False
        else:
            lastBlank = True
        if count == 20:
            break
        

if __name__ == '__main__':
    main()
