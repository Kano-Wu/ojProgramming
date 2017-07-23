#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-23 08:57
Problem: 5-22 龟兔赛跑
https://pta.patest.cn/pta/test/14/exam/4/question/802
'''
t = int(input())

s_tur = 0
s_rab = 0

sleep = False
sleep_time = 1

for ti in range(1, t + 1):
    if sleep == True and sleep_time != 0:
        sleep_time -= 1
        s_rab += 0
    elif sleep == True and sleep_time == 0:
        s_rab += 0
        sleep = False
    else:
        s_rab += 9
    if ti % 10 == 0 and sleep == False and s_rab > s_tur:
        sleep = True
        sleep_time = 29
    s_tur += 3

if s_tur > s_rab:
    print '@_@', s_tur
elif s_rab > s_tur:
    print '^_^', s_rab
else:
    print '-_-', s_tur