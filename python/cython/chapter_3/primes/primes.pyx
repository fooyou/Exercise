#!/usr/bin/env python
# coding: utf-8
# @File Name: primes.pyx
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-12 14:11:16
# @Last Modified: 2017-11-12 18:11:58
# @Description:

cdef primes(int kmax):
    cdef int n, k, i
    cdef int p[1000]
    result = []

    if kmax > 1000:
        kmax = 1000

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

