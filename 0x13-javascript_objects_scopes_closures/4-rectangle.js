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
    [this.width, this.height] = [this.height, this.width];
    for (let i = 0; i < this.height * 2; i++) {
      console.log("X".repeat(this.width * 2));
    }
  }

  double() {
    for (let i = 0; i < this.height * 2; i++) {
      console.log("X".repeat(this.width * 2));
    }
  }
};
