#!/usr/bin/env python
# coding: utf-8

'''
如何进行矩阵和线性代数运算，诸如：矩阵乘法，求解线性方程组，等等？
numpy模块有一个matrix子模块，可以用来处理上述操作。
'''
import numpy as np

m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)

# 转置矩阵A(i, j) = A(j, i)
print(m.T)

# 逆矩阵 AB = BA = E
print(m.I)

# 创建向量并与m相乘
v = np.matrix([[3], [4], [5]])
print(v)

print(m * v)

'''
更多的操作，可以在numpy的子模块linalg中找到
'''

import numpy.linalg as nl

# 矩阵行列式
o = nl.det(m)
print(o)

# 矩阵本征值
o = nl.eigvals(m)
print(o)

# 求解x，mx = v
x = nl.solve(m, v)
print(x)
print(m * x)
print(v)

