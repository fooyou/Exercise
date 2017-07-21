#!/usr/bin/env python
# coding: utf-8
# @File Name: numcalc.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-05-19 10:05:09
# @Last Modified: 2017-05-19 11:05:17
# @Description:

import getopt

def get_opt():
    opts, args = getopt.getopt(sys.argv[1:], "i: 输入文件或文件夹, o: 输出文件夹")
    input_fp = ""
    output_dir = "xls"

    for op, value in opts:
        if op == "-i":
            input_fp = value
        elif op == "-o":
            output_dir = value


