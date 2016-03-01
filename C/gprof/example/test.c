/**
 * @Author: Joshua
 * @E-Mail: liuchaozhen@neusoft.com
 * @Date:   2015-07-23 15:39:26
 * @About test.c
 */

#include <stdio.h>

void func();

void a() {
    printf("Inside a()\n");
    int i = 0;

    for (; i < 0xffffff; ++i);
    func();
    return;
}

static void b() {
    printf("Inside b()\n");
    int i = 0;

    for (; i < 0xffffff; ++i);
    return;
}

int main() {
    printf("Inside main()\n");
    int i = 0;
    for (; i < 0xfffff; ++i);
    a();
    b();
    return 0;
}
