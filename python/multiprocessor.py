#!/usr/bin/env python
# coding: utf-8
# @File Name: multiprocessor.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2018-04-18 14:04:27
# @Last Modified: 2018-04-18 14:04:30
# @Description:
import time
from multiprocessing import Pool
import itertools

def run(fn):
    time.sleep(1)
    return fn * fn


if __name__ == '__main__':
    testFL = [1, 2, 3, 4, 5, 6]

    print("single:")
    s = time.time()
    for i in testFL:
        run(i)

    e = time.time()
    print("single: ", int(e - s))

    print("multiprocessing")
    pool = Pool(processes=5)
    r = pool.map(run, testFL)
    pool.close()
    pool.join()
    e2 = time.time()
    print("multiprocessing: ", int(e2 - e))
    print(r)