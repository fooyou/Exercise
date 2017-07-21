/**
 * @File Name: package.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-17 10:07:55
 * @Last Modified: 2017-07-17 11:07:44
 * @Description:
**/

// 包名
package main

// 导入包
import (
    "fmt"
    "math/rand"
)

/* // python 样式导入，但不推荐使用
import "fmt"
import "math"
*/


/* 包中首字母大写的方法是导出的，可以被包外代码调用 */
func main() {
    fmt.Println("我最喜欢的数字是", rand.Intn(10))
}
