#!/usr/bin/env python
# coding: utf-8
# @File Name: virtualclass.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-08-18 21:08:50
# @Last Modified: 2017-08-20 22:08:02
# @Description:

from abc import ABCMeta, abstractmethod

class Animal(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def say(self):
        pass

    def smile(self):
        print(self.name + ': haha')



class Dog(Animal):

    def say(self):
        print('汪汪')


dog = Dog('dog')
dog.say()
dog.smile()
