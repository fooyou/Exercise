/**
 * @Author: Joshua
 * @E-Mail: liuchaozhen@neusoft.com
 * @Date:   2016-08-10 09:32:59
 * @About stringstream.cpp
 * C++ 标准库中没有 split() 函数的实现，但可以使用 stream 和 strtok
 */

// #include <iostream>
#include <sstream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
    int a[50] = { 0 };
    string lines = "1,4,10,6,7,32,54,232";
    stringstream line(lines);
    string str;
    int i = 0;
    while (getline(line, str, ','))
    {
        stringstream convert;
        convert << str;
        convert >> a[i];
        ++i;
    }
    return 0;
}