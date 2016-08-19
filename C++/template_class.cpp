/**
 * @File Name: template_class.cpp
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2016-08-12 15:08:17
 * @Last Modified: 2016-08-12 16:08:30
 * @Description:
 */

#include <iostream>
using namespace std;

template <class T>
inline const T& max(const T& a, const T& b) {
    return a > b ? a : b;
}

class Op;

ostream& operator<<(ostream &os, const Op &c) {
    os << c.getnum();
    return os;
}

istream& operator >>(istream &is, Op &c) {
    return is;
}

class Op {
public:
    Op(): _num(0) { }
    Op(int n): _num(n) { }
    bool operator >(const Op& a) {
        return _num > a._num;
    }
    int getnum() {return _num;}
    friend ostream& operator <<(ostream &os, const Op &c);
    friend istream& operator >>(istream &is, Op &c);
private:
    int _num;
};


int main() {
    Op a(3), b(4);
    if (a > b)
        cout << "OK" << endl;
    else
        cout << "Haa" << endl;
    cout << ::max(a, b) << endl;
    return 0;
}
