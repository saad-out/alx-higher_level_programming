#!/usr/bin/node
const Square0 = require('./5-square');

class Square extends Square0 {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    if (!this.width || !this.height) {
      return;
    }

    let x = c;
    for (let i = 1; i < this.width; i++) {
      x += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(x);
    }
  }
}

module.exports = Square;
