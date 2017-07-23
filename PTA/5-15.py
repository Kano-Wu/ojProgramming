#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-22 09:49
Problem: 5-15 计算圆周率
https://pta.patest.cn/pta/test/14/exam/4/question/795
'''
theta = float(input())

def fact(k):
    res = 1.0
    for i in range(1, k + 1):
        res = res * i
    return res

def multi(k):
    res = 1.0
    for i in range(1, k + 1):
        res = res * (2 * i + 1)
    return res

sum = 1
for n in range(1, 1000000):
    p = fact(n) / multi(n)
    sum += p
    if p < theta :
        break

pi = sum * 2.0

print '%.6f' % pi