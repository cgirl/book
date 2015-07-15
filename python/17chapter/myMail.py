#!/usr/bin/env python

from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp.qq.com'
POP3SVR = 'pop.qq.com'

origHdrs = ['From: biyj@liaoliao-pay.com', 'To: biyj@liaoliao-pay.com', 'Subject: test msg']
origBody = ['xxx', 'yyy', 'zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs), '\r\n'.join(origBody)])

sendSvr = SMTP(SMTPSVR)
#sendSvr.setdebuglevel(1)
sendSvr.login('biyj@liaoliao-pay.com', 'juanzi1013')
#sendSvr.pass_('juanzi1013')
errs = sendSvr.sendmail('biyj@liaoliao-pay.com', ('biyj@liaoliao-pay.com',), origMsg)

sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)

recvSvr = POP3(POP3SVR)
recvSvr.user('biyj@liaoliao-pay.com')
recvSvr.pass_('juanzi1013')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
sep = msg.index('')
recvBody = msg[sep+1:]
assert origBody == recvBody
