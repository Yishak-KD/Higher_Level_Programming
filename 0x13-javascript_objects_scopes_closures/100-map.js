#!/usr/bin/node
// Script that imports an array and computes with new
let n = require('./100-data').list;
console.log(n);
console.log(n.map((x, y) => x * y));
