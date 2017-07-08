#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-21
Problem: 5-8 超速判断
https://pta.patest.cn/pta/test/14/exam/4/question/788
'''
speed = input()
speed = int(speed)
s = 'OK'
if speed > 60:
    s='Speeding'


print 'Speed: %d - %s' % (speed, s)