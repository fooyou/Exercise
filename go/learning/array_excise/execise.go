/**
 * @File Name: execise.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-17 18:07:50
 * @Last Modified: 2017-07-18 12:07:53
 * @Description:
**/
package main

import "golang.org/x/tour/pic"

func Pic(dx, dy int) [][]uint8 {
    var g [][]uint8
    for i := 0; i < dy; i++ {
        var r []uint8
        for j := 0; j < dx; j++ {
            r = append(r, uint8((i + j) / 2))
        }
        g = append(g, r)
    }
    return g
}

func main() {
    pic.Show(Pic)
}
