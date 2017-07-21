/**
 * @File Name: loop.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-17 12:07:42
 * @Last Modified: 2017-07-17 15:07:49
 * @Description:
**/
package loop

import (
    "fmt"
)

func Loop() {
    // C 风格的 for
    sum := 0
    for i := 0; i < 10; i++ {
        sum += i
    }
    fmt.Println(sum)

    sum = 1
    for ; sum < 100; {
        sum += sum
    }
    fmt.Println(sum)

    // for 就是 while
    sum = 1
    for sum < 100 {
        sum += sum
    }
    fmt.Println(sum)

    // 死循环
    for {
        break
    }
}
