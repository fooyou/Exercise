#!/usr/bin/env python

from numpy import *
import operator


def classify0(inX, dataSet, labels, k):
    '''
    k 近邻分类器
    '''
    dataSetSize = dataSet.shape[0]

    # 距离计算
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndices = distances.argsort()

    # 选择距离最小的 k 个点
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    # 排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def file2matrix(filename):
    '''
    读取数据函数
    '''
    love_directory = {'largeDoses': 3, 'smallDoses': 2, 'didntLike': 1}
    with open(filename) as f:
        arrayOfLines = f.readlines()
        numOflines = len(arrayOfLines)
        returnMat = zeros((numOflines, 3))
        classLabelVector = []
        for i, l in enumerate(arrayOfLines):
            line = l.strip()
            listFromLine = line.split('\t')
            returnMat[i, :] = listFromLine[0:3]
            if listFromLine[-1].isdigit():
                classLabelVector.append(int(listFromLine[-1]))
            else:
                classLabelVector.append(love_directory.get(listFromLine[-1]))

        return returnMat, classLabelVector


def autoNorm(dataSet):
    '''
    归一化函数
    '''
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet /= tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


def datingCLassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('./datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("the classifier came back with: %d, the real answer is %d" % (classifierResult, datingLabels[i]))
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
    print("the total error rate is %f" % (errorCount / float(numTestVecs)))


def classify_person():
    result_list = ['not at all', 'in small doses', 'in large doses']
    percent_tats = float(input('percentage of time spent playing video game?'))
    flied_miles = float(input('frequent flier miles earned per year?'))
    ice_cream = float(input('liters of ice cream consumed per year?'))
    dating_data_matrix, dating_labels = file2matrix('./datingTestSet2.txt')
    normal_matrix, ranges, min_val = autoNorm(dating_data_matrix)
    in_array = array([flied_miles, percent_tats, ice_cream])
    classifier_result = classify0((in_array - min_val) / ranges, normal_matrix, dating_labels, 3)
    print("You will probably like this person: ", result_list[classifier_result - 1])
