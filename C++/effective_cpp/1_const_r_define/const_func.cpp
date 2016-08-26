/**
 * @File Name: main.cpp
 * @Author: Joshua Liu
 * @Email: liuchaozhen@neusoft.com
 * @Create Date: 2016-08-12 14:08:46
 * @Last Modified: 2016-08-26 17:08:49
 * @Description:
 *      mutable 关键字的使用
 */
#include <string>
#include <iostream>

class TextBlcok {
public:
    TextBlcok(const char* s) {
        _text = s;
    }
    std::size_t TextBlcok::length() const {
        // const 成员函数中修改成员变量是不被允许的。
        // 可以给成员变量添加 mutable 修饰就可以总是被修改。
        if (!_lengthInvalid) {
            _textLength = std::strlen(_text);
            _lengthInvalid = true;
        }
        return _textLength;
    }
private:
    std::string _text;
    mutable std::size_t _textLength;
    mutable bool _lengthInvalid;
};

int main() {
    TextBlcok tb("Hello");
    std::cout << tb.length() << std::endl;
    return 0;
}
