#!/usr/bin/node

// function that executes x times a function.

exports.callMeMoby = function (x, theFunction) {
  for (let val = 0; val < x; val += 1) {
    theFunction();
  }
};
