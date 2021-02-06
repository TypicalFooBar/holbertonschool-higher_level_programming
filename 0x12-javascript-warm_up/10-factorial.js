#!/usr/bin/node

function factorial(x) {
	if (isNaN(x) || x == 1)
		return 1
	return x * factorial(x - 1)
}

let result = factorial(parseInt(process.argv[2]))

console.log(result)