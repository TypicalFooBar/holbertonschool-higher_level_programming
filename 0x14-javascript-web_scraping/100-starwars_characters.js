#!/usr/bin/node

const request = require('request')

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (error, response, body) => {
	let data = JSON.parse(body)

	data.characters.forEach(characterUrl => {
		request(characterUrl, (error, response, body) => {
			let character = JSON.parse(body)

			console.log(character.name)
		})
	})
})