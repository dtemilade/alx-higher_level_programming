#!/usr/bin/node

// a class Square that defines a square and inherits from Rectangle

const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let count = 0; count < this.width; count += 1) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
