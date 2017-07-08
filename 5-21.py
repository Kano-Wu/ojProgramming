#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-22 18:05
Problem: 5-21 求特殊方程的正整数解
https://pta.patest.cn/pta/test/14/exam/4/question/801
'''
n = int(input())

def get():
    ok = 0
    for x in range(0, 100):
        for y in range(x, 100):
            if n == x * x + y * y:
                print '%d %d' % (x, y)
                ok = 1
    return ok

if get() == 0:
    print 'No Solution'