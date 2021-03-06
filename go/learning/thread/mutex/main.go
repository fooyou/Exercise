/**
 * @File Name: main.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-31 17:07:26
 * @Last Modified: 2017-07-31 17:07:33
 * @Description:
**/
package main

import (
	"fmt"
	"sync"
	"time"
)

// SafeCounter 的并发使用是安全的
type SafeCounter struct {
	v   map[string]int
	mux sync.Mutex
}

// Inc 增加给定 key 的计数器的值
func (c *SafeCounter) Inc(key string) {
	c.mux.Lock()
	c.v[key]++
	c.mux.Unlock()
}

// Value 返回给定 key 的计数器的当前值
func (c *SafeCounter) Value(key string) int {
	c.mux.Lock()         // lock 之后同一时间只有一个 goruntine 能访问 c.v
	defer c.mux.Unlock() // defer 用来保证互斥锁一定被解锁
	return c.v[key]
}

func main() {
	c := SafeCounter{v: make(map[string]int)}
	for i := 0; i < 100; i++ {
		go c.Inc("somekey")
	}

	time.Sleep(time.Second)
	fmt.Println(c.Value("somekey"))
}
