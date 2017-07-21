package main

/**
 * @File Name: stringers.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-20 11:07:22
 * @Last Modified: 2017-07-20 11:07:52
 * @Description:
**/

import "fmt"

type Person struct {
	Name string
	Age  int
}

func (p Person) String() string {
	return fmt.Sprintf("%v (%v years)", p.Name, p.Age)
}

func main() {
	a := Person{"Joshua Liu", 33}
	z := Person{"Linkin", 34}
	fmt.Println(a, z)
}
