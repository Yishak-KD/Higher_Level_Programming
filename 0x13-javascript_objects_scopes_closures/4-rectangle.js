#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      console.log("X".repeat(this.width));
    }
  }

  rotate() {
    [w, h] = [h, w];
    for (let i = 0; i < h * 2; i++) {
      console.log("X".repeat(w * 2));
    }
  }

  double() {
    for (let i = 0; i < h * 2; i++) {
      console.log("X".repeat(w * 2));
    }
  }
};
