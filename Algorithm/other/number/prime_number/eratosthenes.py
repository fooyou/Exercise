#!/usr/bin/env python
# coding: utf-8
# @File Name: eratosthenes.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-20 19:11:21
# @Last Modified: 2017-11-20 19:11:24
# @Description:
# Eratosthenes 算法求解质数。
#   找出 2~N 的全部质数的方法

def isprime(n):
    vis = [0 for i in range(n)]
    for i in range(2, n):
        for j in range(2 * i, n, i):
            vis[j] = 1
    return vis

print(isprime(10))

