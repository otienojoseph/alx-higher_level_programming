#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        if (c) {
          row += 'C';
        } else {
          row += 'X';
        }
      }
      console.log(row);
    }
  }
}

module.exports = Square;
