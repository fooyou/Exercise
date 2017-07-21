/**
 * @File Name: exercise.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-18 15:07:42
 * @Last Modified: 2017-07-18 15:07:25
 * @Description:
**/
package main

import (
    "golang.org/x/tour/wc"
    "strings"
)

func WordCount(s string) map[string]int {
    map_ret := map[string]int {}
    words := strings.Fields(s)
    for _, word := range words {
        map_ret[word] = map_ret[word] + 1
    }
    return map_ret
}

func Test() {
    wc.Test(WordCount)
}
