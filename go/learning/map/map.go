/**
 * @File Name: map.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-18 12:07:46
 * @Last Modified: 2017-07-18 15:07:55
 * @Description:
**/
package main

import "fmt"

type Vertex struct {
    Lat, Long float64
}

//var m map[string]Vertex

var m1 = map[string]Vertex {
    "Bell Labs": Vertex {
        40.68433, -74.39967,
    },
    "Google": Vertex {
        37.42202, -122.08408,
    },
}

var m2 = map[string]Vertex {
    "Bell Labs": {40.68433, -74.39967},
    "Google": {37.42202, -122.08408},
}

func map_operation() {
    m := make(map[string]int)

    // 插入或更新 map 元素
    m["Beijing"] = 1
    // 获取元素
    elem := m["Beijing"]
    // 测试 key 是否已存在
    elem, exist := m["Beijing"]
    fmt.Println(elem, exist)
    elem, exist = m["Shanghai"]
    fmt.Println(elem, exist)
    // 删除元素
    delete(m, "Beijing")
    elem, exist = m["Beijing"]
    fmt.Println(elem, exist)
}

func main() {
    n := make(map[string]Vertex)
    n["北京"] = Vertex{
        120.00001, -74.39967,
    }
    fmt.Println(m1, m2, n)

    map_operation()
    Test()
}
