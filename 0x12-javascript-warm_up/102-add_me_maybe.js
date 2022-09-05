#!/usr/bin/node
// Function that increments and calls

exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
