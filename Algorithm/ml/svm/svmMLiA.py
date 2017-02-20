#!/usr/bin/env python
# coding: utf-8
# @File Name: svmMLiA.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-02-10 16:02:56
# @Last Modified: 2017-02-10 18:02:42
# @Description:
#   SMO 算法的简单实现。
#   SMO 算法原理：
#       每次循环选择两个 alpha 进行优化，一旦找到一对“合适”的值，界增大其中一个
#   同时减小另外一个。“合适”的原则有两个: 
#           1) 两个 alpha 必须要在间隔边界之外;
#           2) 两个 alpha 还没有进行过区间优化处理或不在边界上;

def loadDataSet():
    dataMat = []
    labelMat = []
    with open('testSet.txt') as f:
        for line in f.readlines():
            lineArr = line.strip().split()
            dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
            labelMat.append(int(lineArr[2]))
    return dataMat, labelMat

def selectJrand(i, m):
    '''
    
    '''
    j = 1
    while j == i:
        j = int(random.uniform(0, m))
    return j;

