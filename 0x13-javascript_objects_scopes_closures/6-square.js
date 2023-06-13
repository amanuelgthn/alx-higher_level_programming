#!/usr/bin/node
// class square that inherits from class rectangle
const classSquare = require('./5-square');

class Square extends classSquare {
  charPrint (c) {
    let i = 0;
    let j = 0;
    let char = c;
    if (c === undefined) {
      char = 'X';
    }
    while (i < this.height) {
      for (j = 0; j < this.height; j++) {
        process.stdout.write(char);
      }
      console.log();
      i++;
    }
  }
}
module.exports = Square;
