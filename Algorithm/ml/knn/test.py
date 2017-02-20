#!/usr/bin/env python
# coding: utf-8
# @File Name: test.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2016-12-22 17:12:14
# @Last Modified: 2016-12-23 11:12:06
# @Description:

import kNN
from numpy import *
# import matplotlib
# import matplotlib.pyplot as plt


# group, labels = kNN.createDataSet()
# print(group, labels)
# k = kNN.classify0([0, 0], group, labels, 3)
# print(k)

# datingMat, datingLabels = kNN.file2matrix('./datingTestSet2.txt')

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingMat[:,1], datingMat[:,2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
# plt.show()

# norm, ranges, minVal = kNN.autoNorm(datingMat)

#kNN.datingCLassTest()

kNN.classify_person()
