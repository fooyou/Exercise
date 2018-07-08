/**
 * @File Name: ipheader.c
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2018-04-20 14:04:47
 * @Last Modified: 2018-04-20 14:04:22
 * @Description:
**/

#include <stdio.h>

typedef struct ip {
    unsigned char ip_hl:4;
    unsigned char ip_v:4;
} ip_header;


int main() {
    printf("%lu\n", sizeof(ip_header));
    return 0;
}
