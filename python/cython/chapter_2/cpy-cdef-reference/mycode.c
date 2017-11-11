/**
 * @File Name: mycodepy.c
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-11-11 21:11:10
 * @Last Modified: 2017-11-11 21:11:15
 * @Description:
**/

#include <stdio.h>
#include "mycode.h"

void printStruct(struct mystruct* s) {
    printf(".string = %s\n", s->string);
    printf(".integer = %i\n", s->integer);
    printf(".string_array = \n");

    int i;
    for (i = 0; i < s->integer; ++i) {
        printf("\t[%i] = %s\n", i, s->string_array[i]);
    }
}
