/**
 * @File Name: array.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-17 16:07:14
 * @Last Modified: 2017-07-17 18:07:09
 * @Description:
 * 数组
 * 类型 [n]T 是一个有 n 个类型为 T 的值的数组。
 *
 * 表达式
 *
 * var a [10]int
 * 定义变量 a 是一个有十个整数的数组。
 *
 * 数组的长度是其类型的一部分，因此数组不能改变大小。 这看起来是一个制约，但是请不要担心； Go 提供了更加便利的方式来使用数组。
**/
package main

import (
    "fmt"
    "strings"
)

func tictac() {
    game := [][]string {
        []string {"_", "_", "_"},
        []string {"_", "_", "_"},
        []string {"_", "_", "_"},
    }

	game[0][0] = "X"
	game[2][2] = "O"
	game[2][0] = "X"
	game[1][0] = "O"
	game[0][2] = "X"

    for i := 0; i < len(game); i++ {
        fmt.Printf("%s\n", strings.Join(game[i], " "))
    }
}

/*
像 python 数组一样访问数组片段
使用 len() 和 cap() 查看 slice 的大小和容量
*/
func slice_literal() {
    names := []string {
        "诸葛孔明",
        "司马懿",
        "百里奚",
        "黒夫",
    }
    fmt.Println(names)
    a := names[:2]
    b := names[1:3]
    c := names[2:]
    fmt.Printf("len=%d cap=%d %v\n", len(a), cap(a), a)
    fmt.Printf("len=%d cap=%d %v\n", len(b), cap(b), b)
    fmt.Printf("len=%d cap=%d %v\n", len(c), cap(c), c)

    a[0] = "刘朝振"
    fmt.Println(names)
}

func printSlice(x []int) {
    fmt.Printf("len=%d cap=%d %v\n", len(x), cap(x), x)
}
/*
添加 slice 元素 func append(s []T, vs ...T) [] T
*/
func slice_append() {
    a := make([]int, 0)
    printSlice(a)
    var b []int
    printSlice(b)
    a = append(a, 1)
    b = append(b, 2, 3, 4, 5)
    printSlice(a)
    printSlice(b)
    //a = append(a, b)
    //printSlice(a)
}

// 遍历 slice
func foreach() {
    pow := []int {1, 2, 4, 8, 16, 32, 64, 128}
    for i, v := range pow {
        fmt.Printf("pow[%d] = %d\n", i, v)
    }
}

func main() {
    var a[2] string
    a[0] = "中国"
    a[1] = "梦"
    fmt.Println(a[0], a[1])
    fmt.Println(a)


    /* 
    Slice
        指向一个序列的值，并包含长度信息
     */
    s := []int{2, 3, 5, 7, 9, 11, 13}
    fmt.Println("s ==", s)
    for i := 0; i < len(s); i++ {
        fmt.Printf("s[%d] == %d\n", i, s[i])
    }

    fmt.Println(len(a))
    fmt.Printf("%T, %T\n", a, s)

    tictac()
    slice_literal()
    slice_append()
    foreach()
}
