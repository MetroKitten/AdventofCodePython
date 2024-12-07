package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	file, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Error Reading File")
	}
	defer file.Close()

	r := bufio.NewReader(file)

	left := []int{}
	right := []int{}

}
