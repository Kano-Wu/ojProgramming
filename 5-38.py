#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-29 15:55
Problem: 5-38 数列求和-加强版
https://pta.patest.cn/pta/test/14/exam/4/question/3006
'''
string = raw_input()
A, N = string.split(' ')
A = int(A)
N = int(N)

num = ''
flag = 0
for i in range(1,N+1)[::-1]:
	temp = A * i + flag
	num += str(temp % 10)
	flag = temp / 10
if flag > 0:
	num += str(flag)
if N == 0:
	print '0'
else:
    print num[::-1]