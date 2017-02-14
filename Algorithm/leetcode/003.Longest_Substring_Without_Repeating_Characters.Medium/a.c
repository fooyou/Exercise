/**
 * @File Name: a.c
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2016-10-27 16:10:35
 * @Last Modified: 2016-11-02 14:11:43
 * @Description:
 *   Given a string, find the length of the longest substring without repeating characters.
 *   Examples:
 *   Given "abcabcbb", the answer is "abc", which the length is 3.
 *   Given "bbbbb", the answer is "b", with the length of 1.
 *   Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
 * @Solution:
 *   使用数组记住当前字符最近出现的位置，一遍算过去，更新左边界，用它计算最大值就行了。需要花费常数空间。
 */
#include <stdio.h>
#include <string.h>

int max(int a, int b) {
    return a > b ? a : b;
}

int lengthOfLongestSubstring(char* s) {
    int maxlen = 0, left = 0, i = 0;
    int sz = strlen(s);
    int prev[256] = { -1 };
    for (; i < sz; ++i) {
        if (prev[s[i]] >= left) {
            left = prev[s[i]] + 1;
        }
        prev[s[i]] = i;
        maxlen = max(maxlen, i - left + 1);
    }

    return maxlen;
}

int main(int argc, char** argv) {
    char *s = "a";
    if (argc > 1)
        s = argv[1];
    printf("%s\n", s);
    int l = lengthOfLongestSubstring(s);
    printf("%d\n", l);
}
