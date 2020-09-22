#!/usr/bin/node
// Define class Rectangle with conditional === 0 or not positive integer
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) && (h = parseInt(h))) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // prints width & height with X
    console.log(
      ('X'.repeat(this.width) + '\n')
        .repeat(this.height)
        .split('')
        .slice(0, -1)
        .join('')
    );
  }

  rotate () {
    // switches width and height
    this.width += this.height;
    this.height = this.width - this.height;
    this.width -= this.height;
  }

  double () {
    // doubles width and height
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
