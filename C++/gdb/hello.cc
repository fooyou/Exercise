/**
 * @File Name: hello.cc
 * @Author: Joshua Liu
 * @Email: liuchaozhen@neusoft.com
 * @Create Date: 2016-04-05 10:04:42
 * @Last Modified: 2016-04-11 17:04:47
 * @Description:
 */
#include <iostream>

double mysqrt(double x)
{
    double y = 1.0;
    while (y * y - x > 0.00001 || x - y * y > 0.00001 )
    {
        y = (y + x / y) * 0.5;
    }
    return y;
}

int main()
{
    double o = mysqrt(999.0);
    std::cout << "o" << std::endl;
    return 0;
}
