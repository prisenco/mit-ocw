package main

import (
	"fmt"
	"math"
)

func main() {
	var x, y float64

	fmt.Print("Enter number x: ")
	fmt.Scan(&x)

	fmt.Print("Enter number y: ")
	fmt.Scan(&y)

	fmt.Println("X**y is", math.Pow(x, y))

	fmt.Println("log(x) is", math.Log2(x))
}
