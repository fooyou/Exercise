/**
 * @File Name: mymath.cc
 * @Author: Joshua Liu
 * @Email: liuchaozhen@neusoft.com
 * @Create Date: 2016-04-06 08:04:21
 * @Last Modified: 2016-04-06 13:04:30
 * @Description:
 */
#include <stdio.h>
#include <stdlib.h>
#include "mymath.h"

const double PRECISE = 0.01;

template <class T>
T myabs(T num) {
    if (num > 0)
        return num;
    if (num < 0)
        return 0 - num;
}

/** 
 * @Brief: 计算数的平方根
 *  1. 目前只实现了大于 1 的正数的求解
 * 
 * @Param: num
 *  输入的数
 * 
 * @Return: 平方根值
 */
double mysqrt(double num) {
    const double i = num;
    if (myabs<double>(i - PRECISE) < 0)
        return num;
    double t = 1;
    int c = 0;
    while (myabs<double>(t * t - i) > PRECISE) {
        c += 1;
        t = t - (t * t / i) + 1;
        fprintf(stdout, "%dth: %f - %f\n", c, num, t);
    }
    return t;
}
