/**
 * @File Name: cast.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-17 12:07:34
 * @Last Modified: 2017-07-17 12:07:27
 * @Description:
**/

package main

import (
    "fmt"
)

func main() {
    var x int = 3
    y := 4
    var f float64 = float64(x)
    u := uint(f)
    fmt.Printf("x %T %v\n", x, x)
    fmt.Printf("y %T %v\n", y, y)
    fmt.Printf("f %T %v\n", f, f)
    fmt.Printf("u %T %v\n", u, u)
}
