#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-21
Problem: 5-6 混合类型数据格式化输入
https://pta.patest.cn/pta/test/14/exam/4/question/786
'''
string = raw_input()
float1, integer, s, float2 = string.split(' ')
float1 = float(float1)
float2 = float(float2)
integer = int(integer)
print '%s %d %.2f %.2f' % (s, integer, float1, float2)