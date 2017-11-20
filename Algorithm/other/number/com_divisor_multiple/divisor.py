#!/usr/bin/env python
# coding: utf-8
# @File Name: divisor.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-20 19:11:30
# @Last Modified: 2017-11-20 19:11:52
# @Description:

def get_gcd(a, b):
    '''
    最小公倍数 = 两整数的乘积 / 最大公约数

    求最大公约数算法：
    有两整数a和b：
    ① a%b得余数c
    ② 若c=0，则b即为两数的最大公约数
    ③ 若c≠0，则a=b，b=c，再回去执行①
    '''
    m = a
    n = b
    c = 0
    while n != 0:
        c = m % n
        m = n
        n = c
    return m, int(a * b / m)

print(get_gcd(15, 10))
