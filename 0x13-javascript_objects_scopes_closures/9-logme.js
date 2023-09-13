#!/usr/bin/node

// function that prints the number of arguments already printed
// and the new argument value

let num = -1;
exports.logMe = function (item) {
  num++;
  console.log(num + ': ' + item);
};
