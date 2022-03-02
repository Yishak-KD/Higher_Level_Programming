#!/usr/bin/node

const { argv } = require("process");

function factorial(num) {
    if (num === 1 || num === NaN) {
        return 1;
    }
    return num * factorial(num-1)
}

console.log(factorial(process.argv[2]));
