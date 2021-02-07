#!/usr/bin/node

const request = require('request')

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (error, response, body) => {
	let obj = JSON.parse(body)
	console.log(obj.title)
})
