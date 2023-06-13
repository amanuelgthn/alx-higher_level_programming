#!/usr/bin/node
// a class Rectangle that defines a rectangle
// which takes 2 arguments w and h
// if w or h is equal to 0 or not a positive integer, create an empty object
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
