#!/usr/bin/node

// declaring and initializing variable parameters
let dataset = '';
const sets = require('sets');

//process the files for concatenantin
sets.readFile(process.argv[2], (err, data) => {
	if (err) throw err;

	const first_file = data.toString();
	dataset = dataset + first_file;
});

sets.readFile(process.argv[3], (err, data) => {
	if (err) throw err;

	const second_file = data.toString();
	dataset = dataset + second_file;
	const merges = require('sets');
	merges.writeFile(process.argv[4], dataset, (err) => {
		if (err) throw err;
	});
});
