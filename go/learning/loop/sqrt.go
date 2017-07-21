/**
 * @File Name: sqrt.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-17 12:07:03
 * @Last Modified: 2017-07-17 15:07:34
 * @Description:
**/
package sqrt

//import (
//    "fmt"
//)

func Sqrt(x float64) float64 {
    const p float64 = 0.00001
    z := 1.0
    for (x - z * z) / (2 * z) > p {
        z = z - (z * z - x) / (2 * z)
    }
    return z
}

//func main() {
//    fmt.Println(Sqrt(2))
//}
