/**
 * @File Name: exercise.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-31 16:07:55
 * @Last Modified: 2017-07-31 17:07:16
 * @Description:
**/
package main

import (
	"fmt"
	"golang.org/x/tour/tree"
)

// Walk 步进 tree t 将所有的值从 tree 发送到 channel ch
func Walk(t *tree.Tree, ch chan int) {
	emit(t, ch)
	close(ch)
}

// emit
func emit(t *tree.Tree, ch chan int) {
	if t != nil {
		emit(t.Left, ch)
		ch <- t.Value
		emit(t.Right, ch)
	}
}

// Same 检测树 t1 和 t2 是否含有相同的值
func Same(t1, t2 *tree.Tree) bool {
	ch1 := make(chan int)
	ch2 := make(chan int)
	go Walk(t1, ch1)
	go Walk(t2, ch2)
	for i := range ch1 {
		if i != <-ch2 {
			return false
		}
	}
	return true
}

func Test() {
	ch := make(chan int)
	n := 1
	go Walk(tree.New(n), ch)
	for v := range ch {
		fmt.Println(v)
	}
	fmt.Println(Same(tree.New(1), tree.New(1)))
	fmt.Println(Same(tree.New(1), tree.New(2)))
}
