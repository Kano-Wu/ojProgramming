#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-21 10:01
Problem: 5-1 厘米换算英尺英寸
https://pta.patest.cn/pta/test/14/exam/4/question/781
'''
cm = input()
cm = int(cm)
meter = cm / 100.0
foot = meter / 0.3048
inch = (foot % 1) * 12
print int(foot), int(inch)