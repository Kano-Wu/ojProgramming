#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-23 16:59
Problem: 5-30 字符串的冒泡排序
https://pta.patest.cn/pta/test/14/exam/4/question/810
'''
text = raw_input()
N, K = text.split(' ')
N = int(N)
K = int(K)
array = []
for i in range(N):
    string = raw_input()
    array.append(string)

for k in range(K):
    for i in range(N - 1):
        if cmp(array[i], array[i + 1]) > 0:
            temp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temp

for i in range(N):
    print array[i]