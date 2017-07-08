#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-23 16:50
Problem: 5-28 猴子选大王
https://pta.patest.cn/pta/test/14/exam/4/question/808
'''
n = input()
ind = []
out = 0
count = 0
for i in range(1, n + 1):
    ind.append(i)

speak = 0
while out < n-1:
    if ind[speak % n] != 0:
        count += 1
    if count == 3:
        count = 0
        ind[speak % n]=0
        out += 1
    speak += 1



for i in range(0, n):
    if ind[i] != 0:
        print ind[i]