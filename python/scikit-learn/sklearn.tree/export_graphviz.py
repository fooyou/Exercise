#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-03-20 14:08:22
# @About export_graphviz.py
#   参见：http://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html
#   
# 函数原型：sklearn.tree.export_graphviz(decision_tree, out_file='tree.dot', feature_names=None,
#   max_depth=None, close=None)
# 功能：把决策树输出成dot格式
# 
# 一旦转成了dot格式，那么就可以转成其他格式了：
#   $ dot -Tps tree.dot -o tree.ps (PostScript format)
#   $ dot -Tpng tree.dot -o tree.png (PNG format)

from sklearn.datasets import load_iris
from sklearn import tree

clf = tree.DecisionTreeClassifier()
iris = load_iris()
clf.fit(iris.data, iris.target)
tree.export_graphviz(clf, out_file='tree.dot')