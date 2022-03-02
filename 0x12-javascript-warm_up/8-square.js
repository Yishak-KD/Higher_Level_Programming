#!/usr/bin/node

const { argv } = require("process");

const a = process.argv[2];
if (isNaN(a)) {
  console.log("Missing size");
} else {
  let string = "";
  for (let i = 0; i < a; i++) {
    for (let j = 0; j < a; j++) {
      string += "X";
    }
    string += "\n";
  }
  console.log(string);
}
