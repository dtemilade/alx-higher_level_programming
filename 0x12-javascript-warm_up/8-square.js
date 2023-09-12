#!/usr/bin/node

// script that prints a square

const count = parseInt(process.argv[2], 10);
if (isNaN(count)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < count; x += 1) {
    console.log('X'.repeat(count));
  }
}
