#!/usr/bin/node

// Count the arguments
let count = -2;
process.argv.forEach((val, index) => {
	count++;

	if (count == 1)
		console.log(val);
});

if (count == 0)
	console.log('No argument');
