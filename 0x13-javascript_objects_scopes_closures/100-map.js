#!/usr/bin/node

// import list from the file 100-data.js
const sets = require('./100-sets').list;

//defining array
const dataset = sets.map(x => x * sets.indexOf(x));

//outputs the initial list and the new list
console.log(sets);
console.log(dataset);
