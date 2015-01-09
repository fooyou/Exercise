/* 
* @Author: joshua
* @Date:   2014-11-04 15:42:25
* @Last Modified by:   joshua
* @Last Modified time: 2014-11-17 16:15:26
*/

#include <iostream>
#include <string>
#include <list>

using std::string;
using std::list;

class A {
public:
    int a;
    int b;
};

/**
 * 
 */
list<string> split(const string& src, const string& delimiter) {
    list<string> result;

    size_t pos = 0;
    string token;
    string s = src;
    while ((pos = s.find(delimiter)) != string::npos) {
        token = s.substr(0, pos);
        result.push_back(token);
        s.erase(0, pos + delimiter.length());
    }
    return result;
}

int main(){
    string src = "HTTP/1.0 200 OK\nServer: SimpleHTTP/0.6 Python/3.4.0\nDate: Tue, 04 Nov 2014 07:54:25 GMT\nContent-type: audio/x-wav\nContent-Length: 862086\nLast-Modified: Sun, 28 Sep 2014 03:31:10 GMT";
    list<string> res = split(src, "\n");

    for (list<string>::iterator it = res.begin(); it != res.end(); ++it) {
        std::cout << *it << std::endl;
    }

    A a;
    a.a = 10;

    return 0;
}