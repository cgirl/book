#!/usr/bin/env python
#coding:utf-8

"find the longest line on the file"

#缺点：文件句柄一致不释放，直到程序运行结束才释放
def Read1():
    f = open('./maxFact.py', 'r')
    longest = 0
    while True:
        linelen = len(f.readline().strip())
#        print 'linelen =', linelen
        if not linelen:
#            print 'while-if'
            break
        if linelen > longest:
#            print 'while-else'
            longest = linelen
    f.close()
    print 'Read1 =', longest

#Read1中使用的是readline,获取一行信息;Read2中使用的是readlines,获取的是整个文章的所有的行
#Read2会在获取所有行之后，就释放了文件句柄
def Read2():
    f = open('./maxFact.py', 'r')
    longest = 0
    allLine = f.readlines()
    f.close()
    for line in allLine:
        linelen = len(line.strip())
        if linelen > longest:
            longest = linelen
    print 'Read2 =', longest

#Read3在获取所有行之前对每行进行拆分，形成一个行列表
#Read2是在循环的时候才进行拆分行
def Read3():
    f = open('./maxFact.py', 'r')
    longest = 0
    allLine = [x.strip() for x in f.readlines()]
    f.close()
    for line in allLine:
        linelen = len(line)
        if linelen > longest:
            longest = linelen
    print 'Read3 =', longest

#Read4不在使用readlines获取所有行，因为文件本身就是一个迭代器，直接使用文件迭代器属性，获取记录每行长度的列表，然后进行列表解析
def Read4():
    f = open('./maxFact.py', 'r')
    allLinelen = [len(x.strip()) for x in f]
    f.close()
    print 'Read4 =', max(allLinelen)

#Read5使用生成器表达式代替列表解析
def Read5():
    f = open('./maxFact.py', 'r')
    print 'Read5 =', max(len(x.strip()) for x in f)
    f.close()

#Read6使用文件打开的默认模式
def Read6():
    print 'Read6 =', max(len(x.strip()) for x in open('./maxFact.py'))


if __name__ == '__main__':
    Read1()
    Read2()
    Read3()
    Read4()
    Read5()
    Read6()
