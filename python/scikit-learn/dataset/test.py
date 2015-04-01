#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-03-19 17:22:42
# @About test.py
import numpy as np
from sklearn import datasets
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

vectorizer = HashingVectorizer(n_features = 10)
tfidf_transformer = TfidfTransformer()

X_train_counts = vectorizer.fit_transform(['武器 大炮', '装备 后勤 投送 机动', '战舰 潜艇', '歼击机 预警机 雷达', 'X光片 肺 健康 慢性炎症', '亚健康 中药 针灸 奇效', '辐射 健康 职业病', '紧急救护 120'])
print(X_train_counts)
x_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
x_train_tags = [1, 1, 1, 1, 2, 2, 2, 2]

classifier = MultinomialNB().fit(x_train_tfidf, x_train_tags)
