#!/usr/bin/node
// class Rectangle that defines a rectangle
class Rectangle {
	constructor (w, h) {
		if ((w > 0) && (h > 0)) {
			this.width = w;
			this.height = h;
		}
	}

	//outputs the result
	print () {
		for (let k = 0; k < this.height; k++) {
			console.log('X'.repeat(this.width));
		}
	}

	rotate () {
		const tmp = this.width;
		this.width = this.height;
		this.height = tmp;
	}

	double () {
		this.width = this.width * 2;
		this.height = this.height * 2;
	}
}

module.exports = Rectangle;
