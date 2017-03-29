/**
 * @File Name: main.c
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-02-22 16:02:24
 * @Last Modified: 2017-02-23 09:02:47
 * @Description:
 *      动态规划方法求最长公共子序列
 */

#include<stdio.h>
#include<string.h>

char a[30];
char b[30];
int lena;
int lenb;
int LCS(int, int);

void main() {
    strcpy(a, "ABCBDAB");
    strcpy(b, "BDCABA");
    lena = strlen(a);
    lenb = strlen(b);
    printf("%d\n", LCS(a, strlen(a), b, strlen(b)));
}
