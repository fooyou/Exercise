#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-07-17 15:44:13
# @About fun_args.py

import sys
import getopt

def check_web_server(host, port, path):
    print(host, port, path)

def daily_sales_total(*all_sales):
    total = 0.0
    for each_sale in all_sales:
        total += float(each_sale)
    print(total)

if __name__ == '__main__':
    host_info_tuple = ('fooyou.github.io', 80, '/')
    check_web_server(*host_info_tuple)

    # **：告诉函数在打开字典时，每个键是参数的名字，对应的值是函数调用的参数。即，这种调用等同于：
    #   check_web_server(host='fooyou.github.io', port=80, path='/')
    host_info_dic = {'host': 'fooyou.github.io', 'port': 80, 'path': '/'}
    check_web_server(**host_info_dic)

    daily_sales_total()
    daily_sales_total(10.00)
    daily_sales_total(5.00, 1.50, '128.57')