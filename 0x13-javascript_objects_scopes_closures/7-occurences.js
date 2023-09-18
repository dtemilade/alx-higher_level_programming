#!/usr/bin/node

// function that returns the number of occurrences in a list:

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const ind in list) {
    if (list[ind] === searchElement) {
      count++;
    }
  }
  return count;
};
