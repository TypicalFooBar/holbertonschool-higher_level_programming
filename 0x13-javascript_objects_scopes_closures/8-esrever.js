#!/usr/bin/node

function esrever(list, searchElement) {
	let newList = []

	list.forEach(value => {
		newList.unshift(value)
	})

	return newList
}

module.exports = {
	esrever
}
