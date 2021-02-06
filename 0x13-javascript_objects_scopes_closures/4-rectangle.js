#!/usr/bin/node

class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}

	print(c = 'X') {
		for (let i = 0; i < this.height; i++)
		{
			let row = '';
			for (let j = 0; j < this.width; j++)
				row += c;

			console.log(row);
		}
	}

	rotate() {
		let temp = this.width
		this.width = this.height
		this.height = temp
	}

	double() {
		this.width *= 2
		this.height *= 2
	}
}

module.exports = Rectangle
