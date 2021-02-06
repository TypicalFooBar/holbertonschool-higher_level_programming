#!/usr/bin/node

const fs = require('fs')

try {
	const fileA = fs.readFileSync(process.argv[2], 'utf8')
	const fileB = fs.readFileSync(process.argv[3], 'utf8')

	fs.writeFileSync(process.argv[4], fileA + "\n" + fileB)
} catch (err) {
	console.error(err)
}
