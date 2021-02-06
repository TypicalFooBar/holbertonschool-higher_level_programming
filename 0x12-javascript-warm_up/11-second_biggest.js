#!/usr/bin/node

let args = [];

process.argv.forEach((value, index) => {
	if (index > 1)
		args.push(value)
});

if (args.length <= 1)
	console.log(0);
else
{
	// Sort the list
	args.sort((a, b) => {
		return b - a;
	})

	console.log(args[1]);
}