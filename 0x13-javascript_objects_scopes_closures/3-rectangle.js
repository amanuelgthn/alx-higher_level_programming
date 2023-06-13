#!/usr/bin/node
// a class Rectangle that defines a rectangle
// which takes 2 arguments w and h
// if w or h is equal to 0 or not a positive integer, create an empty object\
// create an instance method called print() that prints the rectangle using the character x
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let j = 0;
    while (i < this.height) {
      for (j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
      i++;
    }
  }
}
module.exports = Rectangle;
