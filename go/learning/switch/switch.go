/**
 * @File Name: switch.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-17 15:07:39
 * @Last Modified: 2017-07-17 16:07:36
 * @Description:
**/
package main

import (
    "fmt"
    "runtime"
    "time"
)

/* go 的 switch 会自动终止，除非使用 fallthrough 结束 */
func osname() {
    fmt.Print("Go runs on ")
    switch os := runtime.GOOS; os {
    case "darwin":
        fmt.Println("OS X.")
    case "linux":
        fmt.Println("Linux.")
    default:
        fmt.Printf("%s.\n", os)
    }
}

/* switch 会从上到下执行，匹配成功时停止 */
func date() {
    fmt.Println("When's Saturday?")
    today := time.Now().Weekday()
    switch time.Saturday {
    case today + 0:
        fmt.Println("today.")
    case today + 1:
        fmt.Println("Tomorrow.")
    case today + 2:
        fmt.Println("In two days.")
    default:
        fmt.Println("Too far away.")
    }
}

/* 没有条件的 switch 用来替换长的 if-elif-else */
func nocondition() {
    t := time.Now()
    switch {
    case t.Hour() < 12:
        fmt.Println("早上好！")
    case t.Hour() < 17:
        fmt.Println("下午好！")
    default:
        fmt.Println("晚上好！")
    }
}
func main() {
    osname()
    date()
    nocondition()
}
