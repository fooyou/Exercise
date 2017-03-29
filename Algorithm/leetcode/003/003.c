/**
 * @File Name: 003.c
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-03-24 15:03:35
 * @Last Modified: 2017-03-24 15:03:22
 * @Description:
 */

#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char* s) {
    int maxlen = 0, left = 0;
    int sz = strlen(s);
    int prev[256];
    memset(prev, -1, sizeof(prev));

    for (int i = 0; i < sz; ++i) {
        if (prev[s[i]] >= left) {
            left = prev[s[i]] + 1;
        }
        prev[s[i]] = i;
        maxlen = maxlen  > i - left + 1 ? maxlen : i - left + 1;
    }
    return maxlen;
}


int main() {
    char* s = "pwwkew";
    int maxlen = lengthOfLongestSubstring(s);
    printf("%s - %d\n", s, maxlen);
    return 0;
}
