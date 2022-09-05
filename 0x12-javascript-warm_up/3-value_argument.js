#!/usr/bin/node
// Print first argument

const process = require('process');

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
