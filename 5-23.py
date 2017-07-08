#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-23 11:33
Problem: 5-23 币值转换
https://pta.patest.cn/pta/test/14/exam/4/question/803
'''
'''
测试点	结果	得分/满分	用时（ms）	内存（MB）
测试点1	答案正确	8/8	14	3
测试点2	答案正确	4/4	27	3
测试点3	答案正确	3/3	25	3
测试点4	答案错误	0/2	14	3
测试点5	答案正确	3/3	23  3
'''
money = raw_input()

dist = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j'}
upper = {1:'',2: 'S', 3: 'B', 4: 'Q', 5: 'W', 6: 'S', 7: 'B', 8: 'Q',9: 'Y'}
res = ''
length = len(money)

def hasMoreDist(a,b):
    for x in ['1','2','3','4','5','6','7','8','9']:
        if x in money[a + 1 : b]:
            return True
    return False


for i in range(length):
    if length-i > 4:
        b = length - 4
    else:
        b = length
    if money[i] != '0':
        res += dist[money[i]] + upper[length - i]
    elif hasMoreDist(i,b) == True:
        res += dist[money[i]]
    if length - i == 5 and res[-1] != 'W':
        res+='W'

x = res.find('W')
if x - 1 > 0 and res[x - 1] == 'a':
    res=res[0 : x - 2]+res[x : ]

list = []
for s in res.split('a'):
    if s != '':
        list.append(s)

res = 'a'.join(list)
print res