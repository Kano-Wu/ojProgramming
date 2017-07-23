#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-23 13:15
Problem: 5-27 冒泡法排序
https://pta.patest.cn/pta/test/14/exam/4/question/807
'''
text = raw_input()
N, K = text.split(' ')
N = int(N)
K = int(K)
nums = raw_input()
num = nums.split(' ')
for i in range(len(num)):
    num[i] = int(num[i])

for k in range(K):
    for i in range(N - 1):
        if num[i] > num[i + 1]:
            temp = num[i]
            num[i] = num[i + 1]
            num[i + 1] = temp

for i in range(len(num) - 1):
    print num[i],
print num[len(num) - 1]