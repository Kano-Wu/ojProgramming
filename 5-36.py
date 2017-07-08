#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-24 09:39
Problem: 5-36 复数四则运算
https://pta.patest.cn/pta/test/14/exam/4/question/816
'''
string = raw_input()
a1,b1,a2,b2 = string.split(' ')
a1 = float(a1)
b1 = float(b1)
a2 = float(a2)
b2 = float(b2)

def printf(x, y, op=0):
    res = ''
    if op == 1:
        if -0.05 < y < 0.05:
            res = '(%.1f)' % x
        elif -0.05 < x < 0.05:
            res = '(%.1fi)' % y 
        elif y < 0:
            res = '(%.1f%.1fi)' % (x,y)
        else:
            res = '(%.1f+%.1fi)' % (x,y)
    else:
        if y < 0:
            res = '(%.1f%.1fi)' % (x,y)
        else:
            res = '(%.1f+%.1fi)' % (x,y)
    return str(res)

def add(x1,y1,x2,y2):
    x = x1 + x2
    y = y1 + y2
    print printf(x1,y1),'+',printf(x2,y2),'=',printf(x,y,1)[1:-1]
    return

def sub(x1,y1,x2,y2):
    x = x1 - x2
    y = y1 - y2
    print printf(x1,y1),'-',printf(x2,y2),'=',printf(x,y,1)[1:-1]
    return

def mul(x1,y1,x2,y2):
    x = x1 * x2 - y1 * y2
    y = x2 * y1 + x1 * y2
    print printf(x1,y1),'*',printf(x2,y2),'=',printf(x,y,1)[1:-1]
    return

def dev(x1,y1,x2,y2):
    if x2 * x2 + y2 * y2 == 0:
        return
    x = (x1 * x2 + y1 * y2) / (x2 * x2 + y2 * y2)
    y = (x2 * y1 - x1 * y2) / (x2 * x2 + y2 * y2)
    print printf(x1,y1),'/',printf(x2,y2),'=',printf(x,y,1)[1:-1]
    return

add(a1,b1,a2,b2)
sub(a1,b1,a2,b2)
mul(a1,b1,a2,b2)
dev(a1,b1,a2,b2)