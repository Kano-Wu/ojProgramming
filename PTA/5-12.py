#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-21
Problem: 5-12 两个数的简单计算器
https://pta.patest.cn/pta/test/14/exam/4/question/792
'''
string = raw_input()
a, op, b = string.split(' ')
a = int(a)
b = int(b)
if op == '+':
    res = a + b
elif op == '-':
    res = a - b
elif op == '*':
    res = a * b
elif op == '/':
    res = a / b
    if res < 0:
        res += 1
elif op == '%':
    res = a % b
else:
    res = 'ERROR'


print res