#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-23 16:54
Problem: 5-29 删除字符串中的子串
https://pta.patest.cn/pta/test/14/exam/4/question/809
'''
text = raw_input()
sub = raw_input()

while sub in text :
    x = text.find(sub)
    text = text[ : x] + text[x + len(sub) : ]

print text