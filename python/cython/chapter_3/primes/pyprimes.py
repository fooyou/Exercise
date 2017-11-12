#!/usr/bin/env python
# coding: utf-8
# @File Name: pyprimes.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-12 14:11:26
# @Last Modified: 2017-11-12 18:11:34
# @Description:

def primes(kmax):
    n = 0
    k = 0
    i = 0

    if kmax > 1000:
        kmax = 1000

    p = [0] * kmax
    result = []
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i += 1
        if i == k:
            p[k] = n
            k += 1
            result.append(n)
        n += 1
    return result

print(primes(10000))
