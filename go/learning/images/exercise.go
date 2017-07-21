/**
 * @File Name: exercise.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-21 16:07:01
 * @Last Modified: 2017-07-21 16:07:47
 * @Description:
**/
package main

import (
	"golang.org/x/tour/pic"
	"image"
	"image/color"
)

type Image struct{}

func (i Image) ColorModel() color.Model {
	return color.RGBAModel
}

func (i Image) Bounds() image.Rectangle {
	return image.Rect(0, 0, 100, 100)
}

func (i Image) At(x, y int) color.Color {
	return color.RGBA{255, 0, 0, 255}
}

func Exercise() {
	m := Image{}
	pic.ShowImage(m)
}
