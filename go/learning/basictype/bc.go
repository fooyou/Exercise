/**
 * @File Name: bc.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-17 11:07:02
 * @Last Modified: 2017-07-17 11:07:54
 * @Description:
 *  Go 的基本类型有：
 *      bool, string, 
 *      int, int8, int16, int 32, int64
 *      uint, uint8, uint16, uint32, uint64, uintptr
 *      byte // uint8 的别名
 *      rune // int32 的别名，代表一个 Unicode 码
 *      float32, float64
 *      complex64, complex128
**/

package main

import (
    "fmt"
    "math/cmplx"
)

// () 是代码块
var (
    ToBe    bool        = false
    MaxInt  uint64      = 1 << 64 - 1
    z       complex128  = cmplx.Sqrt(-5 + 12i)
)

func main() {
    const f = "%T(%v)\n"
    fmt.Printf(f, ToBe, ToBe)
    fmt.Printf(f, MaxInt, MaxInt)
    fmt.Printf(f, z, z)
}
