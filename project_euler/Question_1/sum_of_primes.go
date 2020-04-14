// Question 1 : The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million.

package main

import (
	"github.com/kavehmz/prime"
)

const limit = 2000000

func main() {
	ps := prime.Primes(limit)
	var sum int
	for i := 0; i < len(ps); i++ {
		sum += i
	}
	println("sum = ", sum)
}
