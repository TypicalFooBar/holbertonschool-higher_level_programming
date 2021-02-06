#!/usr/bin/node

let convertedNumber = parseInt(process.argv[2]);

if (isNaN(convertedNumber))
	convertedNumber = 'Not a number';

console.log(`My number: ${convertedNumber}`);
