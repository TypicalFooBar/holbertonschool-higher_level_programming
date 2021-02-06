#!/usr/bin/node

const Square5 = require("./5-square");

class Square extends Square5 {
	constructor(size) {
		super(size, size)
	}

	charPrint(c) {
		this.print(c);
	}
}

module.exports = Square
