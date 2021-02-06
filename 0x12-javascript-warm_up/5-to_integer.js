#!/usr/bin/node

let convertedNumber = parseInt(process.argv[2]);

if (isNaN(convertedNumber))
	console.log('Not a number');
else
	console.log(`My number: ${convertedNumber}`);
