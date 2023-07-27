#!/usr/bin/node
const file = require('fs');

const data = process.argv[3];

file.writeFile(process.argv[2], data, function (err, data) {
  if (err) console.log(err);
});
