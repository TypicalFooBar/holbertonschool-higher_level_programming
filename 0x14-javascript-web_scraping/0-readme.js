#!/usr/bin/node

const fs = require('fs')

try {
	const fileContents = fs.readFileSync(process.argv[2], 'utf8')
	console.log(fileContents)
} catch (err) {
	console.error(err)
}
