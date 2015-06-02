#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-05-12 15:26:25
# @About test.py
import matplotlib.pyplot as plt

x_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y_list = [0.1, 0.12, 0.2, 0.3, 0.24, 0.35, 0.16, 0.27, 0.18, 0.09]

# plt.subplot(2, 1, 1)
plt.plot(x_list, y_list, 'yo-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.show()