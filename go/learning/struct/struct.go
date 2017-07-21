/**
 * @File Name: struct.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-17 16:07:02
 * @Last Modified: 2017-07-17 16:07:36
 * @Description:
 *
 *  一个结构体（ struct ）就是一个字段的集合。
 *（而 type 的含义跟其字面意思相符。）
**/
package main

import "fmt"

type Vertex struct {
    X int
    Y int
}

var (
    v1 = Vertex{1, 2}
    v2 = Vertex{X: 1}   // Y:0 被省略
    v3 = Vertex{}       // X:0, Y:0
    p = &Vertex{1, 2}   // 类型为 *Vertex
)

func main() {
    fmt.Println(Vertex{1, 2})

    v := Vertex{3, 4}
    fmt.Println(v.X, v.Y)
    v.X = 8
    fmt.Println(v.X, v.Y)

    p := &v
    p.X = 1e9
    fmt.Println(p)
    fmt.Println(v)

    fmt.Println(v1, v2, v3, p)
}
