#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-23 17:53
Problem: 5-33 有理数加法
https://pta.patest.cn/pta/test/14/exam/4/question/813
'''
string = raw_input()
s1,s2 = string.split(' ')
a1,b1 = s1.split('/')
a2,b2 = s2.split('/')
a1 = int(a1)
b1 = int(b1)
a2 = int(a2)
b2 = int(b2)

a = (a1 * b2) + (a2 * b1)
b = b1 * b2

def gcd(a, b):
    g = 1
    m = min(a, b)
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            g = i
    return g

g = gcd(a,b)
a = a / g
b = b / g
if b != 1:
    print '%d/%d' % (a, b)
else:
    print '%d' % a