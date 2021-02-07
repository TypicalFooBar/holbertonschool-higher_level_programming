#!/usr/bin/node

const request = require('request')

function getCharacterNameAsync(characterUrl) {
	return new Promise((resolve, reject) => {
		request(characterUrl, (error, response, body) => {
			if (error)
				reject()
			
			let character = JSON.parse(body)
			resolve(character.name)
		})
	})
}

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, async (error, response, body) => {
	let data = JSON.parse(body)
	let characterNames = []

	for (let i = 0; i < data.characters.length; i++) {
		let name = await getCharacterNameAsync(data.characters[i])
		characterNames.push(name)
	}

	console.log(characterNames)
})