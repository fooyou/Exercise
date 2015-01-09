#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: joshua
# @Date:   2014-11-19 14:47:24
# @Last Modified by:   joshua
# @Last Modified time: 2014-11-19 15:01:27
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, singal):
        super(MyThread, self).__init__()
        self.singal = singal

    def run(self):
        print('%s, will sleep...' %self.name)
        self.singal.wait()
        print('%s, awake...' %self.name)

if __name__ == "__main__":
    singal = threading.Event()
    for t in range(3):
        thread = MyThread(singal)
        thread.start()

    print('main thread sleep 3 seconds...')
    time.sleep(3)

    singal.set()