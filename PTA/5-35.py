#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-29 16:58
Problem: 5-35 有理数均值
https://pta.patest.cn/pta/test/14/exam/4/question/815
'''
'''
测试点	结果	得分/满分	用时（ms）	内存（MB）
测试点1	答案正确	10/10	55	11
测试点2	答案正确	3/3	15	3
测试点3	非零返回	0/5	16	3
测试点4	答案正确	2/2	15	3
'''
def gcd(a,b):
	if a==0 or b==0:
		return 1
	else:
		g = 1
    	m = min(a,b)
    	for i in range(2,m+1):
     	   if a%i==0 and b%i==0:
     	       g=i
    	return g


N = input()
string = raw_input()
fam = string.split(' ')

fa = []
fb = []
for f in fam:
    if '/' in f:
        temp = f.split('/')
        if '' in temp:
        	temp.remove('')
        fa.append(int(temp[0]))
        fb.append(int(temp[1]))

suma = 0
sumb = 1
for b in fb:
    if b == 0:
        continue
    sumb *= b
for i in range(len(fa)):
    if i in range(len(fb)) and fb[i] != 0:
    	suma += fa[i] * (sumb / fb[i])

suma = suma / N

g = 1
if suma < 0:
    ta = -1*suma
    g = gcd(ta, sumb)
else:
    g = gcd(suma, sumb)

if g < 1:
	g = 1
suma = suma / g
sumb = sumb / g

if suma == 0:
    print 0
else:
    if sumb == 1:
        print suma
    else:
        print '%d/%d' % (suma, sumb)