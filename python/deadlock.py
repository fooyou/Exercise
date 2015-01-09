#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: joshua
# @Date:   2014-11-19 14:13:19
# @Last Modified by:   joshua
# @Last Modified time: 2014-11-19 14:19:03
import threading

counterA = 0
counterB = 0

mutexA = threading.Lock()
mutexB = threading.Lock()

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        global mutexA, mutexB
        if mutexA.acquire():
            print('%s, get res: %s' %(self.name, "ResA"))
            if mutexB.acquire():
                print('%s, get res: %s' %(self.name, "ResB"))
                mutexB.release()
            mutexA.release()

    def func2(self):
        global mutexA, mutexB
        if mutexB.acquire():
            print('%s, get res: %s' %(self.name, "ResB"))
            if mutexA.acquire():
                print('%s, get res: %s' %(self.name, "ResA"))
                mutexA.release()
            mutexB.release()

if __name__ == "__main__":
    for i in range(10):
        tmpthread = MyThread()
        tmpthread.start()