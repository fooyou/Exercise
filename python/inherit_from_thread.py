#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: joshua
# @Date:   2014-11-19 13:34:54
# @Last Modified by:   joshua
# @Last Modified time: 2014-11-19 13:42:52
import threading

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setName('My' + self.name)

    def run(self):
        print('Thread name %s' %self.name)


if __name__ == "__main__":
    for thread in range(0, 5):
        t = MyThread()
        t.start()