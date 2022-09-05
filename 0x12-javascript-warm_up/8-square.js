#!/usr/bin/node
// Print a square

const process = require('process');
let string = '';

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    for (let j = 0; j < process.argv[2]; j++) {
      string += 'X';
    }
    string += '\n';
  }
}
console.log(string);
