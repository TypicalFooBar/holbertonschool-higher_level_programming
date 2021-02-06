#!/usr/bin/node

const list = require('./100-data').list;

let newList = [...list];

newList.map((value, index) => {
	newList[index] = value * index
})

console.log(list)
console.log(newList)
