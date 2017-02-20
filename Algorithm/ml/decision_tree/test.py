#!/usr/bin/env python
# coding: utf-8
# @File Name: test.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2016-12-23 16:12:31
# @Last Modified: 2016-12-23 17:12:38
# @Description:
import trees

dataset, labels = trees.create_dataset()
entropy = trees.calc_shannon_entropy(dataset)
print(entropy)
trees.split_dataset(dataset, 0, 0)
