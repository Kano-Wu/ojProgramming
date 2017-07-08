#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-23 18:13
Problem: 5-34 通讯录的录入与显示
https://pta.patest.cn/pta/test/14/exam/4/question/814
'''
N = input()
infos = []

for i in range(N):
    string = raw_input()
    info = string.split(' ')
    infos.append(info)

nums = raw_input()
num = nums.split(' ')
K = num[0]
K = int(K)

s = []

for i in range(K):
    s.append(int(num[i+1]))

for i in range(len(s)):
    if s[i] < N and s[i] > -1:
        print infos[s[i]][0],infos[s[i]][3],infos[s[i]][4],infos[s[i]][2],infos[s[i]][1]
    else:
       print 'Not Found'