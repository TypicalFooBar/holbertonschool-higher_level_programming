#!/usr/bin/node

const request = require('request')
const fs = require('fs')

let count = 0

request(process.argv[2], (error, response, body) => {
	// let data = JSON.parse(body)
	
	try {
		fs.writeFileSync(process.argv[3], body)
	} catch (err) {
		console.error(err)
	}
})