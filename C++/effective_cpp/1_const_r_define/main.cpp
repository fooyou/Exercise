/**
 * @File Name: main.cpp
 * @Author: Joshua Liu
 * @Email: liuchaozhen@neusoft.com
 * @Create Date: 2016-08-12 14:08:46
 * @Last Modified: 2016-08-12 15:08:46
 * @Description:
 */

// #include <stdio.h>
// #include <stdlib.h>
#include <iostream>
using namespace std;

// C++ 中不推荐使用 define
// #define PI 3.14159

// 可以这么写
const double PI = 3.14159;

// 经典的C的宏用法
// #define max(a, b) ((a) > (b) ? (a) : (b))
// 这种宏让人无比痛苦，即便都用了括号还是会出意外
// 所以还是用 inline 函数吧
inline int max(int a, int b) { return a > b ? a : b; }
int main() {
    int a = 5;
    int b = 2;

    // 常规使用没问题
    cout << max(a, b) << endl;

    // 如果碰到++
    cout << max(++a, b) << endl; // 加了2次
    cout << max(++a, b + 10) << endl; // 加了1次

    return 0;
}
