#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-03-17 10:49:40
# @About datasets.py

from sklearn import datasets

iris = datasets.load_iris()
digits = datasets.load_digits()


# digits.data gives access to the features that can be used to classify the digits samples:
# digits.target gives the ground truth for the digit dataset, that is the number
#   corresponding to each digit image that we are trying to learn:
# The data is always a 2D array, shape (n_samples, n_features), although the original data
#   may have had a different shape. In the case of the digits, each original sample is an
#   image of shape (8, 8) and can be accessed using .images[0]
print(iris.data)
print(iris.target)
# print(iris.images[0])

print(digits.data)
print(digits.target)
print(digits.images[0])
