/**
 * @File Name: main.cc
 * @Author: Joshua Liu
 * @Email: liuchaozhen@neusoft.com
 * @Create Date: 2016-04-05 15:04:48
 * @Last Modified: 2016-04-06 11:04:23
 * @Description:
 *      最基础的往往是个可执行的 exe 工程，其 cmake 的编写参见 CMakeLists.txt 文件
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "TutorialConfig.h"
#ifdef USE_MYMATH
#include "mymath.h"
#endif

int main(int argc, char* argv[]) {
    if (argc < 2) {
        fprintf(stdout, "%s 版本号 %d.%d\n",
                argv[0],
                Tutorial_VERSION_MAJOR,
                Tutorial_VERSION_MINOR);
        fprintf(stdout, "用法： %s 数字\n", argv[0]);
        return 1;
    }

    double inputValue = atof(argv[1]);
#ifdef USE_MYMATH
    double outputValue = mysqrt(inputValue);
#else
    double outputValue = sqrt(inputValue);
#endif
    fprintf(stdout, "%g 的平方根是 %g\n", inputValue, outputValue);
    return 0;
}
