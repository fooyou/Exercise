/**
 * @File Name: mycode.h
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-11-11 21:11:49
 * @Last Modified: 2017-11-11 21:11:03
 * @Description:
**/

#ifndef __MYCODE_H__
#define __MYCODE_H__

struct mystruct {
    char* string;
    int integer;
    char** string_array;
};

extern void printStruct(struct mystruct*);

#endif // __MYCODE_H__

