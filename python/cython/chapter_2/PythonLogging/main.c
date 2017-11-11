/**
 * @File Name: main.c
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-11-11 12:11:58
 * @Last Modified: 2017-11-11 12:11:01
 * @Description:
**/

#include "NativeLogging.h"

int main(int argc, const char** argv) {
    if (argc < 2) {
        return -1;
    }

    SetupNativeLogging(argv[1]);

    info("info message");
    debug("debug message");
    error("error message");

    CloseNativeLogging();

    return 0;
}
