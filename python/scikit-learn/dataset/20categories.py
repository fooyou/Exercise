#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-03-27 15:17:33
# @About 20categories.py

from sklearn.datasets import fetch_20newsgroups

##
#  从文本中提取特征向量
##

categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
# print(len(twenty_train.target))

# 对文本分词
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print(X_train_counts.shape)

# tf -idf 'Term Frequency times Inverse Document Frequency'
from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
print(X_train_tf.shape)

# 上面的fit()和transform()可以使用fit_transform()合并
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf.shape)


##
#  训练分类器
##

# 训练分类器Native Bayes
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

# 测试新文档分类
docs_new = ['God is love', 'OpenGL on the GPU is fast']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
predicted = clf.predict(X_new_tfidf)
for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, twenty_train.target_names[category]))

# 由上可见分类器的构建过程: vectorizer => transformer => classifier, 管道可以简化这个过程

##
# 创建管道 pipline
##

from sklearn.pipeline import Pipeline
text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB())
])
text_clf = text_clf.fit(twenty_train.data, twenty_train.target)

##
# 测试集性能评估
##

import numpy as np
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)

# MultinomialNB 正确率
predicted = text_clf.predict(twenty_test.data)
accuracy = np.mean(predicted == twenty_test.target)
print(accuracy)

# SVM 正确率
from sklearn.linear_model import SGDClassifier
text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5, random_state=42))
])
_ = text_clf.fit(twenty_train.data, twenty_train.target)
predicted = text_clf.predict(twenty_test.data)
accuracy = np.mean(predicted == twenty_test.target)
print(accuracy)

# scikit-learn提供了很多分析结果的性能的方法。
from sklearn import metrics
clf_report = metrics.classification_report(twenty_test.target, predicted, target_names=twenty_test.target_names)
print(clf_report)

confusion_matrix = metrics.confusion_matrix(twenty_test.target, predicted)
print(confusion_matrix)