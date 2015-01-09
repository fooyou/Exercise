#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: joshua
# @Date:   2014-11-19 13:46:34
# @Last Modified by:   joshua
# @Last Modified time: 2014-11-19 14:07:09
import threading
import time

counter = 0
mutex = threading.Lock()

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global counter
        time.sleep(1)
        if mutex.acquire():
            counter += 1
            print('%s, set counter: %s' %(self.name, counter))
            mutex.release()

if __name__ == "__main__":
    for i in range(200):
        my_thread = MyThread()
        my_thread.start()