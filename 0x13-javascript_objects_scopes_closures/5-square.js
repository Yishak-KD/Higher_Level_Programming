#!/usr/bin/node

import {Rectangle} form "./4-rectangle.js";
module.exports = class Square extends Rectangle {
    constructor(size) {
        super(w, h);
        this.size = size;
    }
}
