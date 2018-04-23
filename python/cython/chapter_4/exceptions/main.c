/**
 * @File Name: main.c
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-11-13 09:11:37
 * @Last Modified: 2017-11-13 09:11:02
 * @Description:
**/

#include <Python.h>
#include "cycode.h"

int main(int argc, char** argv) {
    Py_Initialize();

    initcycode();
    run();

    Py_Finalize();

    return 0;
}
