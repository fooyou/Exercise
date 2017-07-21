package main

/**
 * @File Name: exercise.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-18 16:07:02
 * @Last Modified: 2017-07-18 16:07:03
 * @Description:
 *		斐波那契闭包
**/
import "fmt"

// fibonacci 函数会返回一个返回 int 的函数。
func fibonacci() func() int {
	x, y := 1, 0
	return func() int {
		y += x
		x = y - x
		return y
	}
}

func Fibonacci() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}
