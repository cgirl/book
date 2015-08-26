#!/usr/bin/env python
#coding:gbk

from operator import add, sub
from random import randint, choice

ops = {'+':add, '-':sub}
MAXTRIES = 2

def doprob():
    op = choice('+-')                           #随机取选项
    nums = [randint(1,10) for i in range(2)]    #生成两个10以内的随机数
    nums.sort(reverse=True)                     #生成的随机数按降序排序
    ans = ops[op](*nums)                        #计算结果
    pr = '%d %s %d = ' % ( nums[0], op, nums[1] )
    oops = 0                                    #错误答案输入次数初始化
    while True:
        try:
            if int(raw_input(pr)) == ans:       #判断答案是否正确
                print 'correct'
                break
            if oops == MAXTRIES:                #超过三次，公布答案
                print 'answer\n%s%d' % (pr, ans)
            else:
                print 'incorrect...try again'   #答案不正确，需要重新回答
                oops += 1
        except (KeyboardInterrupt, EOFError, ValueError):   #异常处理
            print 'invalid...try again'

def main():
    while True:
        doprob()
        try:
            opt = raw_input('Again?[y]').lower()    #所有答案统一转为小写
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == '__main__':
    main()
