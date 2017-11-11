/**
 * @File Name: main.c
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-11-10 21:11:58
 * @Last Modified: 2017-11-10 22:11:57
 * @Description:
**/

#include <Python.h>

int main(int argc, char** argv) {
    // Boiler plate init Python
    Py_SetProgramName(argv[0]);
    Py_Initialize();

    // Init our config mudule into Python memory
    initpublicTest();
    cythonFunction();

    // cleanup python before exit
    Py_Finalize();

    return 0;
}
