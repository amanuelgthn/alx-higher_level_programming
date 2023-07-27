#!/usr/bin/node

const file = require('fs');

file.readFile(process.argv[2], function (err, buf) {
  if (!err) {
    console.log(buf.toString());
  } else {
    console.log(err);
  }
});
