#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: joshua
# @Date:   2014-11-19 14:21:38
# @Last Modified by:   joshua
# @Last Modified time: 2014-11-19 14:28:28
import threading
import time
 
counter = 0
# mutex = threading.Lock()    # 会造成死锁
mutex = threading.RLock()   # 可重入锁，不会造成死锁
 
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
 
    def run(self):
        global counter, mutex
        time.sleep(1);
        if mutex.acquire():
            counter += 1
            print("%s, set counter:%s" % (self.name, counter))
            if mutex.acquire():
                counter += 1
                print("%s, set counter:%s" % (self.name, counter))
                mutex.release()
            mutex.release()
 
if __name__ == "__main__":
    for i in range(10):
        my_thread = MyThread()
        my_thread.start()
