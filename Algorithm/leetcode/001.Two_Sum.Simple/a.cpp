/**
 * @File Name: a.cpp
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2016-10-27 10:10:00
 * @Last Modified: 2016-10-27 11:10:35
 * @Description:
 */
#include <vector>
#include <iostream>
#include <string.h>
using std::vector;
using std::cout;
using std::endl;

/*
 * 使用数组降维
 */
const int OFFSET = 100000;
const int N = 200002;

class Solution {
private:
    int idx_nums[N];

public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        memset(idx_nums, 0, sizeof(idx_nums));
        for (int i = 0; i < nums.size(); ++i) {
            int gap = target - nums[i];
            if (idx_nums[gap + OFFSET]) {
                result.push_back(i);
                result.push_back(idx_nums[gap + OFFSET] - 1);
                break;
            }
            idx_nums[nums[i] + OFFSET] = i + 1;
        }
        return result;
    }
};

int main() {
    vector<int> nums;
    nums.push_back(2);
    nums.push_back(3);
    nums.push_back(9);
    Solution s;
    vector<int> result = s.twoSum(nums, 11);
    for (int i = 0; i < result.size(); ++i)
        cout << result[i] << endl;
    return 0;
}
