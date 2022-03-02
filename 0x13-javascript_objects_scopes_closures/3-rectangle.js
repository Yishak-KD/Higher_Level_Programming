#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    if (this.width > 0 && this.height > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    let string = "";
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        string += "X";
      }
      string += "\n";
    }
    console.log(string);
  }
};
