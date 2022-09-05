#!/usr/bin/node
// Check for integer

const process = require('process');

const number = parseInt(process.argv[2]);

if (number) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
