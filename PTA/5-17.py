#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-29 16:42
Problem: 5-17 爬动的蠕虫
https://pta.patest.cn/pta/test/14/exam/4/question/797
'''
string = raw_input()
temp = string.split(' ')
if '' in temp:
	temp.remove('')

N = int(temp[0])
U = int(temp[1])
D = int(temp[2])

minite = 0
high = 0

while high + U < N:
    high = high + U - D
    minite += 2

print minite + 1