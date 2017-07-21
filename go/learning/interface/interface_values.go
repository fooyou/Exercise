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
	"math"
)

type IF interface {
	M()
}

type TS struct {
	S string
}

func (t *TS) M() {
	if t == nil {
		fmt.Println("<nil>")
		return
	}
	fmt.Println(t.S)
}

type F float64

func (f F) M() {
	fmt.Println(f)
}

func describe(i I) {
	fmt.Printf("(%v, %T)\n", i, i)
}

func InterfaceValues() {
	var i IF
	i = &TS{"Hello"}
	describe(i)
	i.M()

	i = F(math.Pi)
	describe(i)
	i.M()
}

func NilValues() {
	var i IF
	var t *TS
	i = t
	describe(i)
	i.M()
}

func describe_interface(i interface{}) {
	fmt.Printf("(%v, %T)\n", i, i)
}

func EmptyValues() {
	var i interface{}
	describe_interface(i)

	i = 42
	describe_interface(i)

	i = "hello"
	describe_interface(i)
}
