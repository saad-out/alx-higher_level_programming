#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (!this.width || !this.height) {
      return;
    }

    let x = 'X';
    for (let i = 1; i < this.width; i++) {
      x += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(x);
    }
  }

  rotate () {
    if (this.width && this.height) {
      const tmp = this.width;
      this.width = this.height;
      this.height = tmp;
    }
  }

  double () {
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
