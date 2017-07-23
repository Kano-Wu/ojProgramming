#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-23 17:48
Problem: 5-24 约分最简分式
https://pta.patest.cn/pta/test/14/exam/4/question/804
'''
string = raw_input()
a,b = string.split('/')
a = int(a)
b = int(b)

def gcd(a, b):
    g = 1
    m = min(a, b)
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            g = i
    return g

g = gcd(a, b)
a = a / g
b = b / g
print '%d/%d' % (a, b)