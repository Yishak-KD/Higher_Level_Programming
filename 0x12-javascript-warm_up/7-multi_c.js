#!/usr/bin/node
// Print x times

const process = require('process');

if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
