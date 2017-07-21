package main

/**
 * @File Name: assertions.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-19 17:07:57
 * @Last Modified: 2017-07-19 18:07:47
 * @Description:
**/
import "fmt"

func TypeAssertions() {
	var i interface{} = "hello"

	s := i.(string)
	describe(s)

	s, ok := i.(string)
	describe(s)
	describe(ok)

	f, ok := i.(float64)
	describe(f)
	describe(ok)

	//f = i.(float64) // panic 程序会崩溃
	//describe(f)
}

//
// Type switch
//
func do(i interface{}) {
	switch v := i.(type) {
	case int:
		fmt.Printf("interger: %v\n", v)
	case string:
		fmt.Printf("string: %v\n", v)
	default:
		fmt.Printf("unknown type: %T, %v\n", v, v)
	}
}

func TypeSwitch() {
	do(21)
	do("hello")
	do(true)
}

func describe(i interface{}) {
	fmt.Printf("(%v, %T)\n", i, i)
}
