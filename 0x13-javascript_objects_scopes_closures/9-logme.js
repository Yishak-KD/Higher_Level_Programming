#!/usr/bin/node
// Function that prints the number of arguments

let num = 0;
exports.logMe = function (item) {
  console.log(num + ': ' + item);
  num++;
};
