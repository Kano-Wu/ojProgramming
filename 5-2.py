#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-21 16:04
Problem: 5-2 然后是几点
https://pta.patest.cn/pta/test/14/exam/4/question/782
'''
string = raw_input()
start, inter = string.split(' ')
start = int(start)
inter = int(inter)
hour = start / 100
minite = start % 100
minite += inter

if minite > 0:
    if minite > 60:
        hour += minite / 60
        minite = minite % 60
else:
    hour += minite / 60
    minite = minite % 60

print hour * 100 + minite