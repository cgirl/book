#! /usr/bin/env python
# coding=utf-8
#模块文档
"this is a test document"
#模块导入
import sys
import os
#变量定义(全局变量)
debug = True
#类定义
class FooClass(object):
	print 'Foo Class'
	"Foo Class"
	pass
#函数定义
def test():
	"test function"
	print 'test function'
	foo = FooClass()
	if debug:
		print 'ran test()'
#主程序
if __name__ == '__main__':
	print 'ran main'
	test()
	print 'ran over'
