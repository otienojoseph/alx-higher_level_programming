#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1 || !Number.isInteger(h) || !Number.isInteger(w)) {

    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
