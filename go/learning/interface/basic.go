package main

/**
 * @File Name: basic.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-18 18:07:21
 * @Last Modified: 2017-07-18 18:07:41
 * @Description:
 * 接口类型是由一组方法定义的集合。
 * 接口类型的值可以存放实现这些方法的任何值。
**/
import (
	"fmt"
	"math"
)

type Abser interface {
	Abs() float64
}

// float
type float float64

func (f float) Abs() float64 {
	if f > 0 {
		return float64(-f)
	} else {
		return float64(f)
	}
}

// Vertex
type Vertex struct {
	X, Y float64
}

func (v *Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func Basic() {
	var a Abser
	f := float(-math.Sqrt2)
	v := Vertex{3, 4}

	a = f // float 实现了 Abser
	fmt.Println(a.Abs())
	a = &v // *Vertex 实现了 Abser
	fmt.Println(a.Abs())
}
