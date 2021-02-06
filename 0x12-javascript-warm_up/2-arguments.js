#!/usr/bin/node

// Count the arguments
let count = -2;
process.argv.forEach((val, index) => {
	count++;
});

if (count == 0)
	console.log('No argument');
else if (count == 1)
	console.log('Argument found');
else
	console.log('Arguments found');
