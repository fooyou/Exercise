/**
 * @File Name: factorial.cc
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2016-04-12 11:04:48
 * @Last Modified: 2016-04-12 13:04:18
 * @Description:
 */
#include <stdio.h>

int main() {
    int i, num, j = 1;
    printf("输入一个数： ");
    scanf("%d", &num);
    for (i = 1; i <= num; ++i) {
        j = j * i;
    }
    printf("%d 的阶乘是 %d\n", num, j);
}
