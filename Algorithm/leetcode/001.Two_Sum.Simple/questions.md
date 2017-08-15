## 题目

**Two Sum** (Simple) 

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

```
Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

## 题解

1. 先排序再用双指针向中间夹逼，复杂度 O(nlogn)。
2. 用 Map 记录出现的数，使用 target 减去遍历值和 Map 匹配即可，复杂度 O(nlogn) 因为 Map 查询也需要复杂度。
3. 使用数组查询替代 2 中的 Map，这样时间复杂度是 O(n)，但空间复杂度是 O(MAXN)。


## 代码

第三中解法：

- a.c
- a.cpp
- a.py
