#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-21 16:14
Problem: 5-4 BCD解密
https://pta.patest.cn/pta/test/14/exam/4/question/784
'''
num = int(input())
res = num / 16 * 10 + num % 16
print res