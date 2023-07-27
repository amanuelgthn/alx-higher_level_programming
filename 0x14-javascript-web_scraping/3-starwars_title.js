#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const url_id = url + id + '/';
console.log(url_id);
request(url_id, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    const jsonData = JSON.stringify(response);
    const jsonNew = JSON.parse(jsonData);
    const jsonBody = JSON.parse(jsonNew.body);
    console.log(jsonBody.title);
  }
});
