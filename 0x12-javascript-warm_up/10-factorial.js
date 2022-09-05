#!/usr/bin/node
// Compute and print factorial

const process = require('process');

function factorial (a) {
  if (a === 1 || a === undefined) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

console.log(factorial(process.argv[2]));
