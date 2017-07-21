/**
 * @File Name: function.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-17 11:07:03
 * @Last Modified: 2017-07-18 16:07:03
 * @Description:
**/
package main

import "fmt"

func add(x int, y int) int {
	return x + y
}

func add_1(x, y int) int {
	return x + y
}

func swap(x, y string) (string, string) {
	return y, x
}

// 命名返回值
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

func Basic() {
	fmt.Println(add(12, 43))
	fmt.Println(add_1(12, 43))
	a, b := swap("hello", "world")
	fmt.Println(swap("12", "43"))
	fmt.Println(a, b)
	fmt.Println(split(17))
}
