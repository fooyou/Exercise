/* 
* @Author: joshua
* @Date:   2014-11-10 14:57:19
* @Last Modified by:   joshua
* @Last Modified time: 2014-11-17 16:09:58
*/

#include <stdio.h>
#include <stdlib.h>

typedef void (*pfunc)(const char* s);

void printinfo1(const char* s) {
    printf("%s", s);
}

void printinfo2(const char* s) {
    printf("%s", s);
}

void printinfo3(const char* s) {
    printf("%s", s);
}

enum CT {
    _Unknown = -1,
    pt1,
    pt2,
    pt3,
    _TotalNum
};

pfunc callbackfunc[_TotalNum];

typedef unsigned char u8;
typedef u8 ACDI[6];

int main() {
    callbackfunc[pt1] = printinfo1;
    callbackfunc[pt1]("Hello");

    ACDI as = {0};
    printf("%s\n", as);
    return 0;
}