#!/usr/bin/node

const { argv } = require("process");
function add (a, b) {
  return a + b;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
