#!/usr/bin/node
let file = require('fs');

let data = process.argv[3];

file.writeFile(process.argv[2], data, function (err, data) {
  if (err) console.log(err);
});