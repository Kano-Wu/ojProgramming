#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-23 12:55
Problem: 5-25 念数字
https://pta.patest.cn/pta/test/14/exam/4/question/805
'''
num = raw_input()

digist = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si', '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu'}
k = 0
if num[0] == '-':
    print 'fu',
    k = 1

for i in range(k, len(num) - 1):
    print digist[num[i]],

print digist[num[len(num) - 1]]