#!/usr/bin/env python
# coding: utf-8
# @File Name: select.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-10-27 15:10:16
# @Last Modified: 2017-11-09 12:11:27
# @Description:
#   用了下 C 写代码太费劲了，虽然性能好，还是换 Python 吧

import time
import random
import math
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
    冒泡标记排序
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
    '''
    双冒泡
    '''
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
    '''
    插入排序
    '''
    seq = dc(sequence)
    for i in range(1, len(seq)):
        j = i - 1
        while j >= 0 and seq[j] > seq[j + 1]:
            seq[j], seq[j + 1] = seq[j + 1], seq[j]
            j -= 1
    return seq


def insertion_dichotomy_sort(sequence):
    '''
    插入排序+二分查找
    '''
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


def shell_sort(sequence):
    ''' 
    希尔排序的实质就是分组插入排序，本函数是其严格实现
    http://blog.csdn.net/morewindows/article/details/6668714
    '''
    seq = dc(sequence)

    gap = int(len(seq) / 2)
    while gap > 0:
        for i in range(gap):
            for j in range(i + gap, len(seq), gap):
                if seq[j] < seq[j - gap]:
                    temp = seq[j]
                    k = j - gap
                    while k >= 0 and seq[k] > temp:
                        seq[k + gap] = seq[k]
                        k -= gap
                    seq[k + gap] = temp
        gap = int(gap / 2)
    return seq


def shell_improved_sort(sequence):
    '''
    希尔排序优化
    '''
    seq = dc(sequence)

    gap = int(len(seq) / 2)
    while gap > 0:
        for j in range(gap, len(seq)):      # 从第 gap 个元素开始
            if seq[j] < seq[j - gap]:       # 每个元素与自己组内的数据进行直接插入排序
                temp = seq[j]
                k = j - gap
                while k >=0 and seq[k] > temp:
                    seq[k + gap] = seq[k]
                    k -= gap
                seq[k + gap] = temp
        gap = int(gap / 2)
    return seq


def shell_simple_sort(sequence):
    seq = dc(sequence)
    gap = int(len(seq) / 2)
    while gap > 0:
        for i in range(gap, len(seq)):
            j = i - gap
            while j >= 0 and seq[j] > seq[j + gap]:
                seq[j], seq[j + gap] = seq[j + gap], seq[j]
                j -= gap
        gap = int(gap / 2)
    return seq


def shell_dynstep_sort(sequence):
    '''
    希尔排序
    动态改变步长
    '''
    seq = dc(sequence)
    pass


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left):
        result.extend(left)
    if len(right):
        result.extend(right)
    return result


def merge_sort(sequence):
    '''
    归并排序
    '''
    seq = sequence
    if len(seq) < 2:
        return seq
    mid = int(len(seq) / 2)
    left = seq[:mid]
    right = seq[mid:]
    return merge(merge_sort(left), merge_sort(right))


def r_quick_sort(sequence):
    '''
    快排
    '''
    seq = sequence
    if len(seq) < 2:
        return seq
    pivot_idx = int(len(seq) / 2)
    pivot = seq.pop(pivot_idx)
    left = []
    right = []
    for i in range(len(seq)):
        if seq[i] < pivot:
            left.append(seq[i])
        else:
            right.append(seq[i])
    return r_quick_sort(left) + [pivot] + r_quick_sort(right)


def quick_sort(sequence):
    seq = dc(sequence)
    return r_quick_sort(seq)


def heapify(sequence, idx, length):
    seq = sequence
    l = 2 * idx + 1
    r = 2 * idx + 2
    mx = idx
    if l < length and seq[l] > seq[mx]:
        mx = l
    if r < length and seq[r] > seq[mx]:
        mx = r
    if mx != idx:
        seq[idx], seq[mx] = seq[mx], seq[idx]
        heapify(seq, mx, length)


def heap_sort(sequence):
    '''
    堆排序
    '''
    seq = dc(sequence)

    # 建堆
    heapsize= len(seq)
    for i in range(int(heapsize / 2) - 1, -1, -1):
        heapify(seq, i, heapsize)

    # 堆排序
    for i in range(heapsize - 1, 0, -1):
        seq[0], seq[i] = seq[i], seq[0]
        heapsize -= 1
        heapify(seq, 0, heapsize)
    return seq


def couting_sort(sequence):
    '''
    计数排序：只能对整数排序，利用数组下标，且只能排小整数
    '''
    seq = sequence
    C = [0 for _ in range(max(seq) + 1)]
    B = [0 for _ in seq]
    mn = seq[0]
    mx = seq[0]
    for i, c in enumerate(seq):
        mn = mn if mn <= seq[i] else seq[i]
        mx = mx if mx >= seq[i] else seq[i]
        C[seq[i]] = C[seq[i]] + 1 if C[seq[i]] else 1
    for i in range(mn, mx):
        C[i + 1] = C[i + 1] + C[i]
    for i in range(len(seq) - 1, -1, -1):
        B[C[seq[i]] - 1] = seq[i];
        C[seq[i]] -= 1
    return B


def bucket_sort(sequence, num):
    '''
    升级版计数排序
    num: 桶的数量
    '''
    seq = sequence
    mn = seq[0]
    mx = seq[0]
    for i in range(1, len(seq)):
        mn = mn if mn <= seq[i] else seq[i]
        mx = mx if mx >= seq[i] else seq[i]

    buckets = [[] for _ in range(num + 1)]
    space = (mx - mn + 1) / num

    for i in range(len(seq)):
        index = int((seq[i] - mn) / space)
        if buckets[index]:
            k = len(buckets[index]) - 1
            buckets[index].append(seq[i])
            while k >= 0 and buckets[index][k] > seq[i]:
                buckets[index][k + 1] = buckets[index][k]
                k -= 1
            buckets[index][k + 1] = seq[i]
        else:
            buckets[index] = []
            buckets[index].append(seq[i])

    n = 0
    result = []
    while n < num:
        result += buckets[n]
        n += 1
    return result


def radix_sort(sequence, max_digit):
    '''
    基数排序
    '''
    seq = dc(sequence)
    mod = 10
    dev = 1
    counter = []
    for i in range(max_digit):
        for j in range(len(seq)):
            bucket = int((seq[j] % mod) / dev)
            if bucket > len(counter) - 1:
                counter += [[] for _ in range(bucket - len(counter) + 1)]
            counter[bucket].append(seq[j])
        pos = 0
        for j in range(len(counter)):
            while len(counter[j]) > 0:
                seq[pos] = counter[j].pop(0)
                pos += 1
        dev *= 10
        mod *= 10
    return seq


def test_algrithm(sequence, func, *mid):
    start = time.time()
    sorted_seq = func(sequence, *mid)
    print(str((time.time() - start) * 1000.0) + 'ms', func.__name__)
    return sorted_seq


def run_test():
    seq = [random.randint(0, 500) for i in range(20)];
    print(seq)

    # 1.选择排序
    sorted_seq = test_algrithm(seq, select_sort)

    # 2. 冒泡排序
    sorted_seq = test_algrithm(seq, bubble_sort)
    sorted_seq = test_algrithm(seq, bubble_pos_sort)
    sorted_seq = test_algrithm(seq, bubble_double_sort)

    # 3. 插值排序
    sorted_seq = test_algrithm(seq, insertion_sort)
    sorted_seq = test_algrithm(seq, insertion_dichotomy_sort)

    # 4. 希尔排序
    sorted_seq = test_algrithm(seq, shell_sort)
    sorted_seq = test_algrithm(seq, shell_improved_sort)
    sorted_seq = test_algrithm(seq, shell_simple_sort)

    # 5. 归并排序
    sorted_seq = test_algrithm(seq, merge_sort)

    # 6. 快速排序
    sorted_seq = test_algrithm(seq, quick_sort)

    # 7. 堆排序
    sorted_seq = test_algrithm(seq, heap_sort)

    # 8. 计数排序
    sorted_seq = test_algrithm(seq, couting_sort)

    # 9. 桶排序
    sorted_seq = test_algrithm(seq, bucket_sort, 5)
    print(sorted_seq)

    # 10. 基数排序
    sorted_seq = test_algrithm(seq, radix_sort, 3)
    print(sorted_seq)
    print(seq)


if __name__ == '__main__':
    run_test()
