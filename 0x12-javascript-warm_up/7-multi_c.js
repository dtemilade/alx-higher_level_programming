#!/usr/bin/node

// script that prints x times “C is fun”

const count = parseInt(process.argv[2], 10);
if (isNaN(count)) {
  console.log('Missing number of occurences');
} else {
  for (let x = count; x > 0; x -= 1) {
    console.log('C is fun');
  }
}
