#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-22 17:46
Problem: 5-19 支票面额
https://pta.patest.cn/pta/test/14/exam/4/question/799
'''
n = int(input())

def get():
    ok = 0
    for f in range(0,100):
        for y in range(0,100):
            if n == 98 * f - 199 * y:
                print '%d.%d' % (y,f)
                ok = 1
    return ok

if get() == 0:
    print 'No Solution'