/**
 * @Author: Joshua
 * @E-Mail: liuchaozhenyu@gmail.com
 * @Date:   2016-08-12 17:04:57
 * @About operator.cpp
 */

#include <iostream>

using namespace std;

class Complex;

ostream& operator <<(ostream &os, const Complex &c) {
    return os;
}

istream& operator >>(istream &is, Complex &c) {
    return is;
}

class Complex
{
public:
    Complex() : _re(0), _im(0) {}
    Complex(double r, double i) : _re(r), _im(i) { }
    ~Complex() {}

public:
    // 重载输入输出运算符，只能用友元函数
    friend ostream &operator<<(ostream &os, const Complex &c);
    friend istream &operator>>(istream &is, Complex &c);
private:
    double _re;
    double _im;
};


int main(){
    
    return 0;
}