#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    if (this.width > 0 && this.height > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
