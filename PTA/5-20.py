#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-22 18:02
Problem: 5-20 打印九九口诀表
https://pta.patest.cn/pta/test/14/exam/4/question/800
'''
n = int(input())

for x in range(1, n + 1):
    for y in range(1, x + 1):
        if x != y:
            if x * y < 10 :
                print '%d*%d=%d  ' % (y, x, x * y) ,
            else:
                print '%d*%d=%d ' % (y, x, x * y) ,
        else:
            if x * y < 10 :
                print '%d*%d=%d   ' % (y, x, x * y) 
            else:
                print '%d*%d=%d  ' % (y, x, x * y) 