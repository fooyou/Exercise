/* 
* @Author: joshua
* @Date:   2014-11-21 16:37:40
* @Last Modified by:   joshua
* @Last Modified time: 2014-11-21 16:41:26
*/

#include <stdio.h>

typedef struct s_A
{
    int a;
    int b;
} A;

A g_a = {1, 2};

void getStruct(A** p) {
    *p = &g_a;
}

int main() {
    A* p = NULL;
    getStruct(&p);
    if (p) {
        printf("%d\n", p->a);
    }
    return 0;
}