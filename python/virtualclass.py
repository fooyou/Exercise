#!/usr/bin/env python
# coding: utf-8
# @File Name: virtualclass.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-08-18 21:08:50
# @Last Modified: 2017-08-21 10:08:15
# @Description:

from abc import ABCMeta, abstractmethod

class Animal(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name = 'Animal'

    @abstractmethod
    def say(self):
        pass

    def smile(self):
        print(self.name + ': haha')



class Dog(Animal):
    # def __init__(self, name):
    #     self.name = 'Dog'

    def say(self):
        print('汪汪')


dog = Dog('dog')
dog.say()
dog.smile()
print(dog.name)
