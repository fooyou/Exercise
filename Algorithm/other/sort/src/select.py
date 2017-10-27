#!/usr/bin/env python
# coding: utf-8
# @File Name: select.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-10-27 15:10:16
# @Last Modified: 2017-10-27 18:10:08
# @Description:
#   用了下 C 写代码太费劲了，虽然性能好，还是换 Python 吧

import time
import random
from copy import deepcopy as dc

def select_sort(sequence):
    '''
    选择排序
    '''
    seq = dc(sequence)
    for i in range(len(seq) - 1):
        mi = i;
        for j in range(i + 1, len(seq)):
            if seq[j] < seq[mi]:
                mi = j
        seq[i], seq[mi] = seq[mi], seq[i]
    return seq

def bubble_sort(sequence):
    '''
    冒泡排序
    '''
    seq = dc(sequence)
    for i in range(len(seq)):
        for j in range(len(seq) - 1 - i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    return seq

def bubble_pos_sort(sequence):
    '''
    '''
    seq = dc(sequence)
    i = len(seq) - 1
    while i > 0:
        pos = 0
        for j in range(i):
            if seq[j] > seq[j + 1]:
                pos = j
                seq[j], seq[j + 1] = seq[j + 1], seq[j] 
        i = pos
    return seq

def bubble_double_sort(sequence):
    ''' 本以为很好，效果比标注的差太多了 '''
    seq = dc(sequence)
    pos = 0
    neg = len(seq) - 1
    while pos < neg:
        for i in range(pos, neg):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
        neg -= 1
        for j in range(neg, pos, -1):
            if seq[j] < seq[j - 1]:
                seq[j], seq[j - 1] = seq[j - 1], seq[j]
        pos += 1
    return seq

def insertion_sort(sequence):
    seq = dc(sequence)
    for i in range(1, len(seq)):
        key = seq[i]
        j = i - 1
        while j >= 0 and seq[j] > key:
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = key
    return seq


def insertion_dichotomy_sort(sequence):
    ''' 二分查找插入位置 '''
    seq = dc(sequence)
    for i in range(1, len(seq)):
        key = seq[i]
        left = 0
        right = i - 1
        while left <= right:
            mid = int((left + right) / 2)
            if key < seq[mid]:
                right = mid - 1
            else:
                left = mid + 1
        for j in range(i - 1, left - 1, -1):
            seq[j + 1] = seq[j]
        seq[left] = key
    return seq


def test_algrithm(sequence, func):
    start = time.time()
    sorted_seq = func(sequence)
    print(str((time.time() - start) * 1000.0) + 'ms', func.__name__)
    return sorted_seq

if __name__ == '__main__':
    seq = [random.randint(1, 500) for i in range(100)];
    print(seq)
    sorted_seq = test_algrithm(seq, select_sort)
    sorted_seq = test_algrithm(seq, bubble_sort)
    sorted_seq = test_algrithm(seq, bubble_pos_sort)
    sorted_seq = test_algrithm(seq, bubble_double_sort)
    sorted_seq = test_algrithm(seq, insertion_sort)
    sorted_seq = test_algrithm(seq, insertion_dichotomy_sort)
    print(sorted_seq)
