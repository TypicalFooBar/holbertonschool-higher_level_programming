#!/usr/bin/node

let numberOfTimesToPrint = parseInt(process.argv[2]);

if (isNaN(numberOfTimesToPrint))
	console.log('Missing number of occurrences');
else
{
	for (let i = 0; i < numberOfTimesToPrint; i++)
		console.log('C is fun');
}
