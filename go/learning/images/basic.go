/**
 * @File Name: basic.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-21 16:07:32
 * @Last Modified: 2017-07-21 16:07:47
 * @Description:
**/
package main

import (
	"fmt"
	"image"
)

func Baisc() {
	m := image.NewRGBA(image.Rect(0, 0, 100, 100))
	fmt.Println(m.Bounds())
	fmt.Println(m.At(0, 0).RGBA())
}
