#!/usr/bin/node
// class square that inherits from class rectangle
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
