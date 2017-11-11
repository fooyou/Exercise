/**
 * @File Name: main.c
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-11-11 10:11:10
 * @Last Modified: 2017-11-11 10:11:43
 * @Description:
**/

#include <Python.h>
#include "Callback.h"

static void MyCallback(int val) {
    printf("[MYCALLBACK] %i\n", val);
}

int main(int argc, char** argv) {
    // Init Python Runtime
    Py_Initialize();

    // Init callback module
    initCallback();

    // Set callback
    SetCallback(&MyCallback);

    // notify
    Notify(12345);

    // Close Python Runtime
    Py_Finalize();
    return 0;
}
