package main

import (
	"fmt"

	"github.com/ernestosuarez/itertools"
)

const lim = 500

func main() {
	a := []int{}
	for i := 1; i <= lim; i++ {
		a = append(a, i)
	}
	for v := range itertools.CombinationsInt(a, 3) {
		if v[0]*v[0]+v[1]*v[1] == v[2]*v[2] {
			if v[0]+v[1]+v[2] == 1000 {
				mult := 1
				for _, e := range v {
					mult *= e
				}
				fmt.Println("triplets = ", v, "\nsum = ", v[0]+v[1]+v[2], "\nproduct = ", mult)
			}
		}
	}
}
