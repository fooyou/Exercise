package main

/**
 * @File Name: implicity.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-18 18:07:03
 * @Last Modified: 2017-07-18 18:07:53
 * @Description:
**/
import (
	"fmt"
)

type I interface {
	M()
}

type T struct {
	S string
}

// 这个方法意味着 type T 实现了 I，
// 不用显式的声明
func (t T) M() {
	fmt.Println(t.S)
}

func Implicity() {
	var i I = T{"Hello"}
	i.M()
}
