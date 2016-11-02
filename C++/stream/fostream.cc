/**
 * @File Name: fostream.cc
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2016-10-19 17:10:04
 * @Last Modified: 2016-10-19 17:10:01
 * @Description:
 */

#include <iostream>
#include <fstream>
#include <string>

using std::ofstream;
using std::ifstream;
using std::string;
using std::cout;
using std::endl;

int main() {
    // Write to file.
    ofstream of("test");
    of << "Hello World";
    of.close();

    // Read file.
    ifstream fi("test");
    string line;
    if (fi.is_open())
    {
        while (getline(fi, line)) {}
        cout << line << endl;
        fi.close();
    }
    return 0;
}
