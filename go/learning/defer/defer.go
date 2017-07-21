/**
 * @File Name: defer.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-17 16:07:09
 * @Last Modified: 2017-07-17 16:07:35
 * @Description:
 *
 *  defer 语句会延迟函数的执行直到上层函数返回。
 *  延迟调用的参数会立刻生成，但是在上层函数返回前函数都不会被调用。
 *
 *  延迟的函数调用被压入一个栈中。当函数返回时， 会按照后进先出的顺序调用被延迟的函数调用。
**/
package main

import "fmt"

func main() {
    defer fmt.Println("梦")
    fmt.Println("中国")

    fmt.Println("倒计时")
    for i := 1; i < 10; i++ {
        defer fmt.Println(i)
    }
    fmt.Println("完成")
}
