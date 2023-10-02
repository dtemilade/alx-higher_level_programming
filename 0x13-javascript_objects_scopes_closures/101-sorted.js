#!/usr/bin/node

// import dict from the file 101-data.js
const dict = require('./101-data').dict;

//initializing thenew dictionary
const dataset = {};

// declaring keys and values for new dictionary
const keys = Object.values(dict).map(String);
const values = Object.keys(dict).map(String);

//conditional statement for the program
for (let x = 0; x < values.length; x++) {
	if (!dataset[keys[x]]) {
		dataset[keys[x]] = [];
	}
	dataset[keys[x]].push(values[x]);
}

//output the new dictionary
console.log(dataset);
