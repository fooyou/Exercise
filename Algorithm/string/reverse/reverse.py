#!/usr/bin/env python
# coding: utf-8
# @File Name: reverse.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-10 17:11:15
# @Last Modified: 2017-11-10 17:11:43
# @Description:

def reverse(string):
    if string == '':
        return string
    sub_problem = string[1:]
    sub_solution = reverse(sub_problem)
    solution = sub_solution + string[0]
    return solution

print(reverse('Hello world'))
