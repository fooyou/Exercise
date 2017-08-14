/**
 * @File Name: main.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-24 11:07:30
 * @Last Modified: 2017-07-31 16:07:38
 * @Description:
 *  默认情况下，在另一端准备好之前，发送和接收都会阻塞。
 *  这使得 goroutine 可以在没有明确的锁或竞态变量的情况下进行同步。
**/
package main

import "fmt"

func sum(a []int, c chan int) {
	sum := 0
	for _, v := range a {
		sum += v
	}
	c <- sum
}

func basic() {
	a := []int{7, 2, 8, -9, 4, 90}
	c := make(chan int)
	// TODO: 为什么在这里调用会死锁？？
	// sum(a[:len(a)/2], c)
	// fmt.Println(<-c)
	// sum(a[len(a)/2:], c)
	// y := <-c
	// fmt.Println(x, y)

	go sum(a[:len(a)/2], c)
	go sum(a[len(a)/2:], c)
	// x, y = <-c, <-c
	fmt.Println(<-c, <-c)

	// channel 可以带缓冲，只有缓冲满了，才会阻塞
	ch := make(chan int, 3)
	ch <- 1
	ch <- 2
	fmt.Println(<-ch, <-ch)
}

func fibonacci(n int, c chan int) {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		c <- x
		x, y = y, x+y
	}
	close(c)
}

/*
 * 发送者可以 close 一个 channel 来表示再没有值会被发送了。
 * 接收者可以通过赋值语句的第二参数来测试 channel 是否被关闭
 *		v, ok := <-ch
 */
func range_close() {
	c := make(chan int, 10)
	go fibonacci(cap(c), c)
	for i := range c {
		fmt.Println(i)
	}
}

func main() {
	basic()
	range_close()
	Test()
}
