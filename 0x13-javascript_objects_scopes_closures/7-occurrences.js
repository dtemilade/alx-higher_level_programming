#!/usr/bin/node

//declaring the prototype
exports.nbOccurences = function (list, searchElement) {
	let index = 0;

	for (let k = 0; k < list.length; k++) {
		if (list[k] === searchElement) {
			index++;
		}
	}
	return index;
};
