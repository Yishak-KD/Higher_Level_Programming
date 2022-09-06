#!/usr/bin/node
// Return the number of occurences in a list

exports.nbOccurences = function (list, searchElement) {
  let sum = 0;

  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      sum += 1;
    }
  }
  return sum;
};
