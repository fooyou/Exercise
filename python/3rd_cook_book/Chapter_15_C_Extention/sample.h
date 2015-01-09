/* 
* @Author: Joshua
* @Email: liuchaozhen@neusoft.com
* @Date:   2014-11-28 14:23:24
* @Description: 
*/
#ifndef __SAMPLE_H__
#define __SAMPLE_H__

#include <math.h>

extern int gcd(int, int);
extern int in_mandel(double x0, double y0, int n);
extern int divide(int a, int b, int* remainder);
extern double avg(double* a, int n);

typedef struct Point {
    double x, y;
} Point;

extern double distance(Point* p1, Point* p2);

#endif /*__SAMPLE_H__*/