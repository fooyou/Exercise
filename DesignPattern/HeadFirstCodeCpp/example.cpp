/**
 * @File Name: example.cpp
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2016-02-28 09:02:26
 * @Last Modified: 2016-02-28 10:02:05
 * @Description:
 * 测试Graphviz + doxygen 自动生成类图
 */

class Animal {
public:
    void die();
    string name;
    int age;
};

class Dog : public Animal {
public:
    void bark();
};

class Cat : public Animal {
public:
    void meow();
};
