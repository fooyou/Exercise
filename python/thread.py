#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: joshua
# @Date:   2014-11-18 17:16:52
# @Last Modified by:   joshua
# @Last Modified time: 2014-11-19 12:42:55
import time
import threading
import os

def timer(no, interval):
    # cnt = 0
    # while cnt < 3:
    #     print('Thread:', no, 'Time:', time.ctime())
    #     time.sleep(interval)
    #     cnt += 1
    # os.system("echo " + str(no) + ' ' + str(interval))
    print('Thread exit')
    
def test():
    t1 = threading.Thread(target=timer, args=(1, 1))
    t2 = threading.Thread(target=timer, args=(2, 3))

    print(t1.is_alive(), t1.isDaemon(), t1.daemon)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # timer(1, 1)
    # timer(2, 3)

if __name__ == '__main__':
    test()
    print('Main thread exit')