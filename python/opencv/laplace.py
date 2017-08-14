#!/usr/bin/env python
# coding: utf-8
# @File Name: laplace.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-06-15 17:06:04
# @Last Modified: 2017-06-15 17:06:12
# @Description:

import cv2

img = cv2.imread('1.jpg', 0)
img = cv2.GaussianBlur(img, (3, 3), 0)
canny = cv2.Canny(img, 50, 150)

cv2.imshow('Canny', canny)
cv2.waitkey(0)
cv2.destroyAllWindows()

