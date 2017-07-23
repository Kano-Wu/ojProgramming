#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-23 17:40
Problem: 5-32 说反话-加强版
https://pta.patest.cn/pta/test/14/exam/4/question/812
'''
string = raw_input()
words = string.split(' ')

res = ''
for i in range(1, len(words) + 1):
    if words[-i] == '':
        continue
    res += words[-i] + ' '

print res[ : -1]