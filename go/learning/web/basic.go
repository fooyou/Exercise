/**
 * @File Name: basic.go
 * @Author: Joshua Liu
 * @Email: liuchaozhenyu@gmail.com
 * @Create Date: 2017-07-21 16:07:39
 * @Last Modified: 2017-07-21 17:07:31
 * @Description:
**/
package main

import (
	"fmt"
	"log"
	"net/http"
)

type Hello struct{}

func (h Hello) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Hello!")
}

func Basic() {
	var h Hello
	err := http.ListenAndServe("localhost:4444", h)
	if err != nil {
		log.Fatal(err)
	}
}
