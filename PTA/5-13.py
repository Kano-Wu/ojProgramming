#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-21
Problem: 5-13 日K蜡烛图
https://pta.patest.cn/pta/test/14/exam/4/question/793
'''
string = raw_input()
op, hi, lo, cl = string.split(' ')

op = float(op)
hi = float(hi)
lo = float(lo)
cl = float(cl)

if cl < op:
    res = 'BW-Solid'
elif cl > op:
    res = 'R-Hollow'
else:
    res = 'R-Cross'

if lo < op and lo < cl and  hi > op and hi > cl:
    res += ' with Lower Shadow and Upper Shadow'
elif lo < op and lo < cl:
    res += ' with Lower Shadow'
elif hi > op and hi > cl:
    res += ' with Upper Shadow'

print res