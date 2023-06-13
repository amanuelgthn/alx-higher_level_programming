#!/usr/bin/node
// class square that inherits from class rectangle
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i = 0;
    let j = 0;
    let char = c;
    if (c === undefined) {
      char = 'X';
    }
    while (i < this.height) {
      for (j = 0; j < this.width; j++) {
        process.stdout.write(char);
      }
      console.log();
      i++;
    }
  }
}
module.exports = Square;
