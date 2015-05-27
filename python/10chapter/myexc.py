#!/usr/bin/env python
#coding:gbk

import os, socket, errno, types, tempfile

#忽略网络错误信息，基类是IOError
class NetworkError(IOError):
    pass

#忽略文件错误信息，基类是IOError
class FileError(IOError):
    pass

#自定义函数:更新异常参数
def updArgs(args, newarg=None):
    #继承原有的异常参数
    if isinstance(args, IOError):
        myargs = []
        myargs.extend([arg for arg in args])
    else:
        myargs = list(args)

    #追加自定义的异常参数
    if newarg:
        myargs.append(newarg)

    return tuple(myargs)


#文件错误参数更新
def fileArgs(file, mode, args):
    if args[0] == errno.EACCES and 'access' in dir(os):
        perms = ''
        permd = { 'r':os.R_OK, 'w':os.W_OK, 'x':os.X_OK}
        pkeys = permd.keys()
        pkeys.sort()
        pkeys.reverse()

        for eachPerm in 'rwx':
            if os.access(file, permd[eachPerm]):
                perms += eachPerm
            else:
                perms += '-'
    
        if isinstance(args, IOError):
            myargs = []
            myargs.extend([arg for arg in args])
        else:
            myargs = list(args)
        myargs[1] = "['%s'] [%s] [(perms:'%s')]" % (mode, myargs[1], perms)
        myargs.append(args.filename)
    else:
        myargs = args

    return tuple(myargs)

#网络连接程序
def myconnect(sock, host, port):
    try:
        sock.connect((host, port))
    except socket.error, args:
        myargs = updArgs(args)
        if len(myargs) == 1:
            myargs = (errno.ENXIO, myargs[0])

        raise NetworkError, updArgs(myargs, host+':'+str(port))

#文件程序
def myopen(file, mode = 'r'):
    try:
        fo = open(file, mode)
    except IOError, args:
        raise FileError, fileArgs(file, mode, args)
    return fo

#文件测试程序
def testfile():
    file = tempfile.mktemp()
    f = open(file, 'w')
    f.close()
    for eachTest in ((0, 'r'), (0100, 'r'), (0400, 'w'), (0500, 'w')):
        try:
            os.chmod(file, eachTest[0])
            f = myopen(file, eachTest[1])
        except FileError, args:
            print "%s:%s" % (args.__class__.__name__, args)
        else:
            print file, "opened ok... perm ignored"
            f.close()
    os.chmod(file, 0777)
    os.unlink(file)

#网络连接测试程序
def testnet():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for eachHost in ('host', 'www'):
        try:
            myconnect(s, eachHost, 8080)
        except NetworkError, args:
            print "%s:%s" % (args.__class__.__name__, args)
        else:
            print "ok -> %s" % eachHost

#主程序测试
if __name__ == '__main__':
    testfile()
    testnet()

