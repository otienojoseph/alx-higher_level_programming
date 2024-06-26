#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1 || !Number.isInteger(h) || !Number.isInteger(w)) {
      return null;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
