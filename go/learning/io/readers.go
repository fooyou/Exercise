/**
 * @File Name: readers.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-21 15:07:18
 * @Last Modified: 2017-07-21 15:07:54
 * @Description:
 *	io 包指定了 io.Reader 接口， 它表示从数据流结尾读取。
 *	Go 标准库包含了这个接口的许多实现， 包括文件、网络连接、压缩、加密等等
 *
**/
package main

import (
	"fmt"
	"io"
	"strings"
)

func ReaderBasic() {
	r := strings.NewReader("Hello, Reader!")
	b := make([]byte, 8)
	for {
		n, err := r.Read(b)
		fmt.Printf("n = %v err = %v b = %v\n", n, err, b)
		fmt.Printf("b[:n] = %q\n", b[:n])
		if err == io.EOF {
			break
		}
	}
}
