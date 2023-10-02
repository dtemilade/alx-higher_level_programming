#!/usr/bin/node

//declaring Prototype
exports.converter = function (base) {
	return function (num) {
		return num.toString(base);
	};
};
