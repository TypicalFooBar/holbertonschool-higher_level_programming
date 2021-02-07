#!/usr/bin/node

const request = require('request')

let count = 0

request(process.argv[2], (error, response, body) => {
	let data = JSON.parse(body)
	data.results.forEach(film => {
		film.characters.forEach(characterUrl => {
			if (characterUrl.includes("18"))
				count++
		})
	})

	console.log(count)
})