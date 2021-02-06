#!/usr/bin/node

const list = require('./100-data').list;

let newList = [];

list.forEach(value => {
	newList.push(value)
})

newList.map((value, index) => {
	newList[index] = value * index
})

console.log(list)
console.log(newList)
