#!/usr/bin/node

// declaring and initializing variable parameters
let dataset = '';
const dict = require('dict');

//process the files for concatenantin
dict.readFile(process.argv[2], (err, data) => {
	if (err) throw err;

	const first_file = data.toString();
	dataset = dataset + first_file;
});

sets.readFile(process.argv[3], (err, data) => {
	if (err) throw err;

	const second_file = data.toString();
	dataset = dataset + second_file;
	const merges = require('dict');
	merges.writeFile(process.argv[4], dataset, (err) => {
		if (err) throw err;
	});
});
