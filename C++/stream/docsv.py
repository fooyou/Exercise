#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2016-08-10 10:06:33
# @About docsv.py

import sys
import csv

if __name__ == '__main__':
    rows = [];
    with open('data.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for line in reader:
            rows.append(line)

    for i, line in enumerate(rows):
        if i > 0:
            rows[i][5] = str(int(line[2]) + int(line[3]) + int(line[4]))
            if int(line[2]) < 60 or int(line[3]) < 60 or int(line[4]) < 60:
                rows[i][0] = line[0] + '*'
            names = []
            for name in line[1].split(' '):
                names.append(name.capitalize())
            rows[i][1] = ' '.join(names)

    with open('result.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"')
        writer.writerows(rows)