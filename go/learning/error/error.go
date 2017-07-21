package main

/**
 * @File Name: error.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-20 12:07:06
 * @Last Modified: 2017-07-20 12:07:31
 * @Description:
 *		error 和 string 是 fmt 的内置的接口
 *		原型为：
 *			type error interface {
 *				Error() string
 *			}
**/

import (
	"fmt"
	"strconv"
	"time"
)

type MyError struct {
	When time.Time
	What string
}

func (e *MyError) Error() string {
	return fmt.Sprintf("at %v %s", e.When, e.What)
}

func run() error {
	return &MyError{
		time.Now(),
		"it didn't work",
	}
}

func anotherCase(s string) {
	i, err := strconv.Atoi(s)
	if err != nil {
		fmt.Printf("couldn't convert number: %v\n", err)
		return
	}
	fmt.Println("Converted integer:", i)
}

func Basic() {
	if err := run(); err != nil {
		fmt.Println(err)
	}

	anotherCase("32")
	anotherCase("a32")
}
