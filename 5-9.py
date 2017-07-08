#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-21
Problem: 5-9 用天平找小球
https://pta.patest.cn/pta/test/14/exam/4/question/789
'''
string = raw_input()
a, b, c = string.split(' ')
a = int(a)
b = int(b)
c = int(c)
if a == b:
    print 'C'
elif b == c:
    print 'A'
elif a == c:
    print 'B'