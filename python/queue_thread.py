#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2016-07-11 14:42:47
# @About queue_thread.py
import threading
import time
from queue import Queue

lists = [12, 43, 21, 2, 6, 7, 9, 45, 12, 56]

def thread_proc(queue):
    while not queue.empty():
        item = queue.get()
        time.sleep(0.5)
        print(threading.current_thread(), item)
        # queue.task_done()

if __name__ == '__main__':
    q = Queue()
    for item in lists:
        q.put(item)

    

    thread_list = []
    for i in range(2):
        thread = threading.Thread(target=thread_proc, args=(q,))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()
    # q.join()