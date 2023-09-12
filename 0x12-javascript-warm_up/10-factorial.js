#!/usr/bin/node
const retval = parseInt(process.argv[2], 10);
function factorial (retval) {
  if (isNaN(retval) || retval === 0) {
    return (1);
  }
  return (retval * factorial(retval - 1));
}
console.log(factorial(retval));
