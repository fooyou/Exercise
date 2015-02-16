#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-02-09 14:29:36
# @About demo.py
#   Levenshtein是用于文本或字符串距离以及相似度计算的工具，本脚本用户其接口的测试和学习。

from Levenshtein import *

# editops(source_string, destination_string):
# editops(edit_operations, source_length, destination_length)
#   把src变成dest需要进行的操作
#   
# apply_edit(edit_operations, source_string, destination_string):
#   编辑操作一个序列并应用到String
e = editops('man', 'scotsman')
print(e)
print(apply_edit(e, 'man', 'scotsman'))
print(apply_edit(e[:3], 'man', 'scotsman'))

# distance(string1, string2):
#   计算字符串之间的距离
print(distance('振朝刘', '朝刘平玲'))

# hamming(string1, string2): 
#   两字符串必须长度相同（不同会异常），然后比较distance即为hamming
print(hamming('振朝刘', '朝刘平'))

# inverse(edit_operations)
#   对edit operation进行反序，也就是说，src->dest的操作可以变成dest->src的操作
print(editops('振朝刘', '朝刘平'))
print(inverse(editops('振朝刘', '朝刘平')))

# jaro(string1, string2)
#   计算Jaro字符串的相似度系数, 1为完全一致，0为完全不同
#   注意：Jaro是为短小的字符串设计的，比如外国人名姓氏
print(jaro('Jeshua', 'Joshua'))
print(jaro('Jeshua', 'J'))

# jaro_winkler(string1, string2[, prefix_weight])
#   Jaro_Winkler字符串相似度系数是jaro的改进版，可以自定义前缀权重,默认值是0.1
print(jaro_winkler('Jeshua', 'Jeshoa', 0.25))
print(jaro_winkler('Jeshua', 'J', 0.6))


# matching_blocks(edit_operations, source_length, destination_length)
#   在两字符串中找相同的子块
#   第2,3个参数可以是实际字符串，也可以是字符串长度
#   Note：最后有一个长度为0的块输出是为了和difflib兼容，非是bug
a, b = 'Jeshua', 'Joshua'
print(matching_blocks(editops(a, b), a, b))
mb = matching_blocks(editops(a, b), len(a), len(b))
print(mb)
# 打印出相同的字符
print(''.join([a[x[0]:x[0] + x[2]] + ' ' for x in mb]))
print(''.join([b[x[0]:x[0] + x[2]] + ' ' for x in mb]))


# median(string_sequence[, weight_sequence])
#   使用贪心算法在多个相似字符串中找到找到合适的广义中性字符串(Generalized median string)
#   第二个参数为各个字符串的自定义权重值
fixme1 = ['SpSm', 'mpamm', 'Spam', 'Spa', 'Sua', 'hSam']
fixemeweigt = [10, 10, 5, 6, 10, 10]
print(median(fixme1, fixemeweigt))
fixme2 = ['Levnhtein', 'Leveshein', 'Leenshten', 'Leveshtei', 'Lenshtein', 'Lvenstein', 'Levenhtin', 'evenshtei']
print(median(fixme2))

# median_improve(string, string_sequence[, weight_sequence])
#   median的改进版，根据给定的第1个参数string，计算median string
print(median_improve(median(fixme1), fixme2))
print(ratio('Brian', 'Jesus'))
