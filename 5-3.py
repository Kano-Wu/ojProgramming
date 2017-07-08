#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-21 16:10
Problem: 5-3 逆序的三位数
https://pta.patest.cn/pta/test/14/exam/4/question/783
'''
num = int(input())
res = 0
while num > 0:
    res += num % 10
    num = num / 10
    if num > 0:
        res = res * 10

print res