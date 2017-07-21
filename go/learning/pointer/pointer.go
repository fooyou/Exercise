/**
 * @File Name: pointer.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-17 16:07:32
 * @Last Modified: 2017-07-17 16:07:25
 * @Description:
 *  Go 的指针和 C 一样，但没有指针运算
**/
package main

import (
    "fmt"
)

func main() {
    i, j := 42, 2701

    p := &i         // 指向 i 的指针
    fmt.Println(*p) // 读取指针指向内容
    *p = 21         // 修改指针指向内容
    fmt.Println(i) // 读取指针指向内容

    p = &j
    *p = *p / 27

    fmt.Println(j)
}
