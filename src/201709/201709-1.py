#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
试题编号：	201709-1
试题名称：	打酱油
时间限制：	1.0s
内存限制：	256.0MB
问题描述：
问题描述
　　小明带着N元钱去买酱油。酱油10块钱一瓶，商家进行促销，每买3瓶送1瓶，或者每买5瓶送2瓶。请问小明最多可以得到多少瓶酱油。
输入格式
　　输入的第一行包含一个整数N，表示小明可用于买酱油的钱数。N是10的整数倍，N不超过300。
输出格式
　　输出一个整数，表示小明最多可以得到多少瓶酱油。
样例输入
40
样例输出
5
样例说明
　　把40元分成30元和10元，分别买3瓶和1瓶，其中3瓶送1瓶，共得到5瓶。
样例输入
80
样例输出
11
样例说明
　　把80元分成30元和50元，分别买3瓶和5瓶，其中3瓶送1瓶，5瓶送2瓶，共得到11瓶。


'''

#解法一：递归
num = int(input())
n = num//10 # "//"运算取整时保留整数的下界，即偏向于较小的整数

def buy_sauce(n): #递归实现
    if n == 0: #不足10
        return 0
    if n == 1: # 10-19
        return 1
    if n == 2: #20-29
        return 2
    if n == 3: #30-39
        return 4
    if n == 4: #40-49
        return 5
    if n == 5: #50-59
        return 7
    if n>5: # >=60
        x = buy_sauce(n-5)+7 #减去50再进行下一轮递归计算buy_sauce(n-5)
    return x
print(buy_sauce(n))

#解法二：循环
n = int(input())
count = 0 #瓶数count
while n != 0: #三种情况：>=50、30-49、<30
    if n >= 50:
        n -= 50
        count += 7
        continue
    if n >= 30 and n < 50:
        n -= 30
        count += 4
        continue
    if n < 30:
        count += int(n/10)
        n = 0
 
print(count)

#解法二CCF截图
"""由上图，该方法也可以得到正确结果且满足要求，可以看作解法一的变体，其实没有改变多少。为什么呢？
      定性的来看：如上面所说，每个if下返回的都是指定值且只有一处if进行递归调用。
      定量的来看：当定额小于50元时，解法一第一次函数执行即返回结果，解法二循环体while执行一次就推出循环输出结果；当大于等于50时，解法一buy_sauce函数递归调用了多少次，解法二while循环体对应也执行了多少次。
"""
#解法三：运用数学知识进行累加
n = int(input())
count = 0

if n >= 50: #算出有多少个50元
    t = int(n/50)
    n -= t*50
    count += t*7

if n >= 30:#如果剩下还有30多元
    n -= 30
    count += 4

count += int(n / 10)#不足30元

print(count)
"""
这个方法就是分三段进行计算：>=50、30-49、<30，然后进行累加最后输出。
"""