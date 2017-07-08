#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-23 13:05
Problem: 5-26 单词长度
https://pta.patest.cn/pta/test/14/exam/4/question/806
'''
text = raw_input()
text = text[ : len(text) - 1]
words = text.split(' ')
length = []
for word in words:
    if word != '':
        length.append(len(word))
if len(length) != 0:
    for i in range(len(length) - 1):
        print length[i],
    print length[len(length) - 1]