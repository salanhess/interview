package main

// refer to https://github.com/astaxie/build-web-application-with-golang/blob/master/zh/02.5.md
import (
	"fmt"
)

type Human struct {
	name  string
	age   int
	phone string
}

type Student struct {
	Human
	School string
}

type Empoyee struct {
	Human
	ltd string
}

func (s Human) sayHi() {
	fmt.Printf("Human %s age is %d and tel is %s\n", s.name, s.age, s.phone)
}

func (s Empoyee) sayHi() {
	fmt.Printf("Empoyee %s work at %s,age is %d and tel is %s\n", s.name, s.ltd, s.age, s.phone)
}
func main() {
	s1 := Student{Human{"Carol", 21, "138XXX"}, "CSU"}
	s1.sayHi()
	e1 := Empoyee{Human{"Carol", 36, "138XXX"}, "JD"}
	e1.sayHi()
}
