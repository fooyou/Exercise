package main

/**
 * @File Name: rot13reader.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-21 15:07:24
 * @Last Modified: 2017-07-21 15:07:23
 * @Description:
**/
import (
	"io"
	"os"
	"strings"
)

type rot13Reader struct {
	r io.Reader
}

func (r *rot13Reader) Read(b []byte) (int, error) {
	in, err := r.r.Read(b)
	if err != io.EOF {
		for i := 0; i < len(b); i++ {
			if b[i] != ' ' {
				if b[i] >= 'A' && b[i] <= 'Z' {
					if b[i]+13 <= 'Z' {
						b[i] += 13
					} else {
						b[i] -= 13
					}
				} else if b[i] >= 'a' && b[i] <= 'z' {
					if b[i]+13 <= 'z' {
						b[i] += 13
					} else {
						b[i] -= 13
					}
				}
			}
		}
	}
	return in, err
}

func ExeRot13() {
	s := strings.NewReader("Lbh penpxrq gur pbgr!")
	r := rot13Reader{s}
	io.Copy(os.Stdout, &r)
}
