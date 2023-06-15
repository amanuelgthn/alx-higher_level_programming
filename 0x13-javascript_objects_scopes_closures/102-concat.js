#!/usr/bin/node
// a script that concats two files
// 1st argument is the file path of the first source file
// 2nd argument is the file path of the second source file
// 3rd argument is the file path of the destination
const fs = require('fs');
const args = process.argv;
let i = 2;
for (; i < 4; i++) {
  fs.readFile(args[i], 'utf-8', (err, data) => {
    if (err) throw err;
    else {
      if (i === 2) {
        fs.write(args[4], data, null, (err) => {
          if (err) throw err;
        });
      } else {
        fs.appendFile(args[4], data, (err) => {
          if (err) throw err;
        });
      }
    }
  });
}
