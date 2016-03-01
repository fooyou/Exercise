/**
 * @Author: Joshua
 * @E-Mail: liuchaozhen@neusoft.com
 * @Date:   2015-07-23 15:39:26
 * @About func.c
 */

#include <stdio.h>

void func() {
    printf("Inside func\n");
    int i = 0;

    for (; i < 0xffffff; ++i);
    return;
}
