#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-22 10:57
Problem: 5-16 求符合给定条件的整数集
https://pta.patest.cn/pta/test/14/exam/4/question/796
'''
a = int(input())

c = a + 3

list = []
for x in range(a, c + 1):
    for y in range(a, c + 1):
        for z in range(a, c + 1):
            if x != y and x != z and y != z:
                list.append(x * 100 + y * 10 + z)


list.sort()

for i in range(1, len(list) + 1):
    if i % 6 == 0:
        print list[i - 1]
    else:
        print list[i - 1],