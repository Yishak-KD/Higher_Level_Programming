#!/usr/bin/node
// Script that imports a dictionary of occurrences

let dict = require('./101-data').dict;
let n = {};
for (let i in dict) {
  if (n[dict[i]] === undefined) {
    n[dict[i]] = [];
  }
  n[dict[i]].push(i);
}
console.log(n);