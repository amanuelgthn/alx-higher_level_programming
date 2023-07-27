#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
console.log(url);
request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: %s', response.statusCode);
  }
});
