#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: joshua
# @Date:   2014-11-19 12:50:49
# @Last Modified by:   joshua
# @Last Modified time: 2014-11-19 13:32:22
import threading

def thread_fun(num):
    for i in range(int(num)):
        print(threading.currentThread().getName(), 'num:', i)

def main(thread_num):
    thread_list = []

    # 创建线程对象
    for i in range(thread_num):
        thread_name = 'thread_%s' %i
        thread_list.append(threading.Thread(target = thread_fun, name = thread_name, args = (10,)))

    # 启动所有线程
    for thread in thread_list:
        thread.start()

    # 主线程中等待所有子线程退出
    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    main(3)