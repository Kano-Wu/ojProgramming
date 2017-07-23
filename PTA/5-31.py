#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-23 17:04
Problem: 5-31 字符串循环左移
https://pta.patest.cn/pta/test/14/exam/4/question/811
'''
string = raw_input()
N = input()

string = string[N % len(string) : ] + string[ : N % len(string)]

print string