#!/usr/bin/env python
# coding: utf-8
# @File Name: trees.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2016-12-23 16:12:31
# @Last Modified: 2017-01-07 15:01:32
# @Description:
#

from math import log
import operator


def create_dataset():
    dataset = [[1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [1, 0, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataset, labels


def calc_shannon_entropy(dataset):
    '''
    计算信息熵
    '''
    num_entries = len(dataset)
    label_counts = {}

    # 为所有可能分类创建字典
    for d in dataset:
        cur_label = d[-1]
        if cur_label not in label_counts.keys():
            label_counts[cur_label] = 0
        label_counts[cur_label] += 1

    shannon_entropy = 0.0
    for key in label_counts:
        prob = float(label_counts[key]) / num_entries
        shannon_entropy -= prob * log(prob, 2)

    return shannon_entropy


def split_dataset(dataset, axis, value):
    '''
    按 value 和 axis 重分 dataset
    '''
    result_dataset = []
    for d in dataset:
        if d[axis] == value:
            reduced_data = d[:axis]
            reduced_data.extend(d[axis + 1 :])
            result_dataset.append(reduced_data)

    return result_dataset


def choose_best_feature_to_split(dataset):
    '''
    选择最好特征划分的索引值
    '''
    num_features = len(dataset[0]) - 1      # 最后一列是 label
    base_entropy = calc_shannon_entropy(dataset)
    best_infogain = 0.0
    best_feature = -1

    # 遍历所有的特征
    for i in range(num_features):
        # 创建特征列表
        feature_list = [d[i] for d in dataset]
        # 使用 set 确保特征值列表唯一
        unique_values = set(feature_list)

        # 计算某特定值的信息熵
        new_entropy = 0.0
        for v in unique_values:
            subdataset = split_dataset(dataset, i, v)
            prob = len(subdataset) / float(len(dataset))
            new_entropy += prob * calc_shannon_entropy(subdataset)
        
        info_gain = base_entropy - new_entropy
        if info_gain > best_infogain:
            best_infogain = info_gain
            best_feature = i

    return best_feature

def majority_count(class_list):
    class_count = {}
    for v in class_list:
        if v not in class_count.keys():
            class_count[v] = 0
        class_count[v] += 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def create_tree(dataset, labels):
    class_list = [v[-1] for v in dataset]

    # 如果所有元素值相同
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]

    # 如果每行只有一个元素
    if len(dataset[0]) == 1:
        return majority_count(class_list)

    best_feature = choose_best_feature_to_split(dataset)
    best_feature_label = labels[best_feature]
    dtree = {best_feature_label:{}}
    del(labels[best_feature])
    feature_values = [v[best_feature] for v in dataset]
    unique_values = set(feature_values)
    for v in unique_values:
        sub_labels = labels[:]
        dtree[best_feature_label][v] = create_tree(split_dataset(dataset, best_feature, v), sub_labels)

    return dtree


