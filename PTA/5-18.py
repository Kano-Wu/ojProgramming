#-*- coding: utf-8 -*-
'''
Author: Kano Wu
Time: 2017-03-22 14:59
Problem: 5-18 二分法求多项式单根
https://pta.patest.cn/pta/test/14/exam/4/question/798
'''
'''
测试点	结果	得分/满分	用时（ms）	内存（MB）
测试点1	答案正确	12/12	17	3
测试点2	答案正确	3/3	16	3
测试点3	答案正确	3/3	16	3
测试点4	运行超时	0/2	0	0
'''
string = raw_input()
a3,a2,a1,a0 = string.split(' ')
a3 = float(a3)
a2 = float(a2)
a1 = float(a1)
a0 = float(a0)

string = raw_input()
a,b = string.split(' ')
a = float(a)
b = float(b)

def f(x):
    return a3 * pow(x, 3) + a2 * pow(x, 2) + a1 * x + a0

f_a = f(a)
f_b = f(b)
if f_a == 0:
    print '%.2f' % a
elif f_b == 0:
    print '%.2f' % b
else:
    while True:
        mid = (a + b) / 2
        f_mid = f(mid)
        if f_mid == 0:
            print '%.2f' % mid
            break
        elif f_mid < 0:
            if f_a >0:
                b = mid
                f_b = f_mid
            elif f_b >0:
                a = mid
                f_a = f_mid
        else:  #f_mid>0
            if f_a < 0:
                b = mid
                f_b = f_mid
            elif f_b < 0:
                a = mid
                f_a = f_mid
