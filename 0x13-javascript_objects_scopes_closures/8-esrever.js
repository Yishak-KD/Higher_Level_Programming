#!/usr/bin/node
exports.esrever = function (list);

function esrever(list) {
    let string = new Array;
    for (let i = (list.length - 1); i >= 0; i--) {
        string.push(list[i])
    }
    return string;
}
