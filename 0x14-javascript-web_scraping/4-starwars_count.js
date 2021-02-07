#!/usr/bin/node

const request = require('request')

let count = 0

request(`https://swapi-api.hbtn.io/api/films`, (error, response, body) => {
	let data = JSON.parse(body)
	data.results.forEach(film => {
		if (film.characters.includes("https://swapi-api.hbtn.io/api/people/18/"))
			count++
	})

	console.log(count)
})