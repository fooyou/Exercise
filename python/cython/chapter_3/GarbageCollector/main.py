#!/usr/bin/env python
# coding: utf-8
# @File Name: main.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-11 22:11:22
# @Last Modified: 2017-11-11 22:11:27
# @Description:
from PyData import Data


def TestPythonData():
    # Looks and feels like normal python objects
    objectList = [Data(1), Data(2), Data(3)]

    # Print them out
    for d in objectList:
        print(d)

    # Show the Mutability
    objectList[1].SetValue(1234)
    print(objectList[1])

    # all native objects will be deallocated on close
    pass

if __name__ == '__main__':
    TestPythonData()
