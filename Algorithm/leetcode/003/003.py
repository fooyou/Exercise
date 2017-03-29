#!/usr/bin/env python
# coding: utf-8
# @File Name: 003.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-03-24 14:03:22
# @Last Modified: 2017-03-24 14:03:59
# @Description:

import unittest

def lengthOfLongestSubstring(s):
    res = 0
    left = 0
    d = {}

    for i, ch in enumerate(s):
        if ch in d and d[ch] >= left:
            left = d[ch] + 1
        d[ch] = i
        res = max(res, i - left + 1)
    return res

class mytest(unittest.TestCase):
    def testLengthOfLongestSubstring(self):
        max_len = lengthOfLongestSubstring('abcabcbb')
        self.assertEqual(max_len, 3)

if __name__ == '__main__':
    unittest.main()
