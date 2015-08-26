#!/usr/bin/env python
#coding=gbk
import os

for tmpdir in ('./'):
    if os.path.isdir(tmpdir):
        break
    else:
        print 'no temp directory available'
        tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)    #改变当前工作目录，进入到tmpdir指定的目录下
    cwd = os.getcwd()   #获取当前工作目录
    print '*** current temporary directory'
    print cwd

print '*** creating example directory'
print cwd

print '*** current temporary directory...'
os.mkdir('example')     #创建目录
os.chdir('example')     #进入到创建的目录中
cwd = os.getcwd()       #获取当前工作目录
print '*** new working directory:'
print cwd
print '*** original directory listing:'
print os.listdir(cwd)   #列出指定目录的文件

print '*** creating test file...'
fobj = open('test.txt', 'w')#创建一个test.txt文件
fobj.write('foo\n')         #写入内容foo
fobj.write('bar\n')         #写入内容bar
fobj.close()                #关闭文件描述符
print '*** updated directory listing：'
print os.listdir(cwd)       #列出当前目录下的所有文件




