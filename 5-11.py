#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-21
Problem: 5-11 分段计算居民水费
https://pta.patest.cn/pta/test/14/exam/4/question/791
'''
ton = input()
ton = float(ton)
if ton > 15:
    mon = 2.5 * ton - 17.5
else:
    mon = 4.0 * ton / 3


print '%.2f' % mon