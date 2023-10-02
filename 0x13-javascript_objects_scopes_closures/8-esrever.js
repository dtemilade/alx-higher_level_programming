#!/usr/bin/node

//declaring the prototype
exports.esrever = function (list) {
	const retval = [];

	//conditional statement
	for (let k = list.length - 1; k >= 0; k--) {
		retval.push(list[k]);
	}
	return retval;
};
