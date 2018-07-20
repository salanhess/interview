package main

import (
	"fmt"
	//"runtime"
)

type Element interface{}
type List []Element

func main() {
	var x byte = 1
	var y rune = 1111
	list := make(List, 3)
	list[0] = x
	list[1] = y
	for index, element := range list {
		switch value := element.(type) {
		case uint8:
			fmt.Printf("list[%d] type is %s and value is %d\n", index, "byte", value)
		case int32:
			fmt.Printf("list[%d] type is %s and value is %d\n", index, "rune", value)
		case nil:
			fmt.Printf("list[%d] type is %s and value is Empty\n", index, "nil")
		default:
			fmt.Printf("list[%d] unexpected type for %s", index, value)
		}
	}
}
