/**
 * @File Name: main.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-24 11:07:41
 * @Last Modified: 2017-07-24 11:07:06
 * @Description:
 *	goroutine 是 Go 运行时环境管理的轻量级线程
 *		go f(x, y, ...)
 *	开启一个新的 goroutine 执行，goroutine 在相同的地址空间中运行，
 *  因此访问共享内存必须进行同步。sync 提供了这种可能，不过在 Go
 *  中并不经常用到，因为有其他的办法。
 *
**/
package main

import (
	"fmt"
	"time"
)

func say(s string) {
	for i := 0; i < 5; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(s)
	}
}

func main() {
	go say("world")
	say("hello")
}
