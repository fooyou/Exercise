package main

/**
 * @File Name: exercise.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-21 15:07:47
 * @Last Modified: 2017-07-21 15:07:15
 * @Description:
 *	io.Reader 接口的练习
**/
import "golang.org/x/tour/reader"

type MyReader struct{}

func (r MyReader) Read(b []byte) (int, error) {
	for i := 0; i < len(b); i++ {
		b[i] = 'A'
	}
	return len(b), nil
}

func Exercise() {
	reader.Validate(MyReader{})
}
