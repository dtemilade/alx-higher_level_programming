#!/usr/bin/node

// a class Rectangle that defines a rectangle:
module.exports = class Rectangle {
  constructor (myWidth, myHeight) {
    if (myWidth > 0 && myHeight > 0) {
      this.width = myWidth;
      this.height = myHeight;
    }
  }

  print () {
    for (let count = 0; count < this.height; count += 1) {
      console.log('X'.repeat(this.width));
    }
  }
};
