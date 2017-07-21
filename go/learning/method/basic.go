/**
 * @File Name: basic.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-18 17:07:08
 * @Last Modified: 2017-07-18 18:07:34
 * @Description:
**/
package main

import (
	"fmt"
	"math"
)

/*
 * Go 没有类。但仍可在结构体类型上定义方法。
 */
type Vertex struct {
	X, Y float64
}

func (v *Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func vertex_test() {
	v := &Vertex{3.14159, 1}
	fmt.Println(v.Abs())
}

/*
 * 可对包中任意类型定义方法
 * 除了基础类型和其他包的类型
 */
type float float64

func (f float) Abs() float64 {
	if f < 0 {
		return float64(-f)
	} else {
		return float64(f)
	}
}

func float_test() {
	f := float(-math.Sqrt2)
	fmt.Println(f.Abs())
}

/*
 * 接受者为指针的方法
 */
func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func scale_test() {
	v := &Vertex{3, 4}
	fmt.Printf("prev scale: %+v, Abs: %v\n", v, v.Abs())
	v.Scale(1.5)
	fmt.Printf("next scale: %+v, Abs: %v\n", v, v.Abs())
}

func Basic() {
	vertex_test()
	float_test()
	scale_test()
}
