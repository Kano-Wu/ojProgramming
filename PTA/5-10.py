#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-21
Problem: 5-10 计算工资
https://pta.patest.cn/pta/test/14/exam/4/question/790
'''
string = raw_input()
year, hour = string.split(' ')
year = int(year)
hour = float(hour)
if year < 5:
    mon = 30
else:
    mon = 50

if hour > 40:
    salary = mon * 40 + mon * (hour - 40) * 1.5
else:
    salary = mon * hour

print '%.2f' % salary