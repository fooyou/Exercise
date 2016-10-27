/**
 * @File Name: a.c
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2016-10-27 10:10:00
 * @Last Modified: 2016-10-27 11:10:34
 * @Description:
 */
#include <stdio.h>
#include <stdlib.h>

/*
 * 使用数组降维
 */
#define OFFSET 100000
#define N 200002

int* twoSum(int* nums, int numSize, int target) {
    int* result = (int*)malloc(2 * sizeof(int));
    int idx_nums[N] = { 0 };
    for (int i = 0; i < numSize; ++i) {
        int gap = target - nums[i];
        if (idx_nums[gap + OFFSET]) {
            result[0] = i;
            result[1] = idx_nums[gap + OFFSET] - 1;
            break;
        }
        idx_nums[nums[i] + OFFSET] = i + 1;
    }
    return result;
}

int main() {
    int nums[] = { 1, 5, 7, 9};
    int* result = twoSum(nums, sizeof(nums), 14);
    printf("%d %d\n", result[0], result[1]);
    free(result);
    return 0;
}
