# !/usr/bin/env python
# @File Name: a.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2016-10-27 11:10:03
# @Last Modified: 2016-10-27 14:10:54
# @Description:
# 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        for i, n in enumerate(nums):
            if target - n in mapping:
                return [i, mapping[target - n]]
            mapping[n] = i


if __name__ == '__main__':
    nums = [2, 3, 6]
    sol = Solution()
    print(sol.twoSum(nums, 9))
        
