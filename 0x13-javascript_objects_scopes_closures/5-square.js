#!/usr/bin/node

module.exports = class Square extends Rectangle {
    constructor(size) {
        super(w, h);
        this.size = size;
    }
}
