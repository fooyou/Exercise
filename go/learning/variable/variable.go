/**
 * @File Name: variable.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-17 11:07:16
 * @Last Modified: 2017-07-17 11:07:12
 * @Description:
**/
package main

import "fmt"

// 声明
// var c, python, java bool
// 声明 初始化
var c, python, java = true, true, "no!"

func main() {
    var i int
    fmt.Println(i, c, python, java)

    // := 为简洁赋值语句，用在明确类型的地方
    // k := 3
    hungery, thirsty, angry, happy, note := true, true, true, false, "你大爷的"
    fmt.Println(hungery, thirsty, angry, happy, note)
}
