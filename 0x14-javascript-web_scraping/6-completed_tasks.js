#!/usr/bin/node

const request = require('request')
const fs = require('fs')

let usersWithCompletedTasks = {}

request(process.argv[2], (error, response, body) => {
	let data = JSON.parse(body)

	data.forEach(task => {
		if (task.completed == true) {
			if (usersWithCompletedTasks[task.userId] === undefined)
				usersWithCompletedTasks[task.userId] = 1
			else
				usersWithCompletedTasks[task.userId] += 1
		}
	})

	console.log(usersWithCompletedTasks)
})