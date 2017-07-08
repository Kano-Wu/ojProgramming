#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-21
Problem: 5-7 12-24小时制
https://pta.patest.cn/pta/test/14/exam/4/question/787
'''
string = raw_input()
hour, minite = string.split(':')
hour = int(hour)
minite = int(minite)
s = 'AM'
if hour > 12:
    if hour == 24:
        hour = 0
        s = 'AM'
    else:
        s = 'PM'
        hour = hour - 12
else:
    if hour == 12:
        s = 'PM'

print '%d:%d %s' % (hour, minite, s)