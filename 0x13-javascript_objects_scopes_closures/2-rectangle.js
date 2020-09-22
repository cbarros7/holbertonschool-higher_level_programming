#!/usr/bin/node
// Define class Rectangle with conditional === 0 or not positive integer
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) && (h = parseInt(h))) > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
