/**
 * @File Name: main.cpp
 * @Author: Joshua Liu
 * @Email: liuchaozhen@neusoft.com
 * @Create Date: 2016-08-12 14:08:46
 * @Last Modified: 2016-08-25 10:08:19
 * @Description:
 */

#include <string>
#include <iostream>

class TextBlcok {
public:
    TextBlcok(const char* s) {
        text = s;
    }
    const char& operator[] (std::size_t position) const {
        std::cout << "const operator[]  ";
        return text[position];
    }
    char& operator[] (std::size_t position) {
        std::cout << "non-const operator[]  ";
        return text[position];
    }
private:
    std::string text;
};

int main() {
    TextBlcok tb("Hello");
    std::cout << tb[0] << std::endl;
    const TextBlcok ctb("World");
    std::cout << ctb[0] << std::endl;
    return 0;
}
