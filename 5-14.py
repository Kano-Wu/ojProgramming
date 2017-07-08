#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-22 09:18
Problem: 5-14 求整数段和
https://pta.patest.cn/pta/test/14/exam/4/question/794
'''
string = raw_input()
a, b = string.split(' ')

a = int(a)
b = int(b)

i = 0
s = 0
for x in range(a, b + 1):
    i+=1
    s+=x
    if i % 5 == 1:
        print '%5d' % x ,
    elif i % 5 == 0:
        print '%4d' % x
    else:
        print '%4d' % x ,
if i % 5 != 0:
    print

print 'Sum = %d' % s