# -*- coding: utf-8 -*-
# @Author: Joshua Liu
# @Date:   2018-06-05 17:34:37
# @Last Modified by:   Joshua Liu
# @Last Modified time: 2018-06-06 14:05:48
import random

array = [(0, 900), (1, 88), (2, 86), (3, 75), (4, 74), (5, 71), (6, 10), (7, 8), (0, 900), (1, 88), (2, 86), (3, 75), (4, 74), (5, 71), (6, 10), (7, 8)]
def random_by_weight(array):
    num = len(array) // 2
    total_weight = 0
    prehalf_weight = 0
    for i, (k, v) in enumerate(array):
        total_weight += v
        if i < num:
            prehalf_weight += v
    prehalf_count = int(round((1.0 * prehalf_weight / total_weight) * num))
    nxthalf_count = num - prehalf_count
    print(prehalf_count, nxthalf_count)

    out_array = []
    tmp_array = random.sample(array[:num], prehalf_count)
    out_array.extend(tmp_array)
    tmp_array = random.sample(array[num:], nxthalf_count)
    out_array.extend(tmp_array)
    out_array = sorted(out_array, key=lambda x:x[1], reverse=True)
    print(out_array)

if __name__ == '__main__':
    random_by_weight(array)
