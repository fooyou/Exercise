/**
 * @File Name: a.c
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2016-10-27 16:10:35
 * @Last Modified: 2016-10-27 18:10:18
 * @Description:
 *   Given a string, find the length of the longest substring without repeating characters.
 *   Examples:
 *   Given "abcabcbb", the answer is "abc", which the length is 3.
 *   Given "bbbbb", the answer is "b", with the length of 1.
 *   Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
 */
#include <stdio.h>

int lengthOfLongestSubstring(char* s) {
    int length = 0;
    char* begin = s;
    char* end = begin;
    char* cur = begin;
    char* t = NULL;
    char b = 0;
    if (*cur != '\0') {
        while (*(++cur) != '\0') {
            for (t = begin + 1; t <= end; ++t) {
                if (*t == *cur) {
                    b = 1;
                    break;
                }
            }
            if (*cur == *begin)
                ++begin;
            end = b ? end : cur;
        }
        length = end - begin + 1;
    }
    printf("%s %d\n", begin, length);
    return length;
}

int main() {
    char *s = "abba";
    printf("%s\n", s);
    int l = lengthOfLongestSubstring(s);
    // char *s1 = "abcabcbb";
    // l = lengthOfLongestSubstring(s1);
    printf("%d\n", l);
}
