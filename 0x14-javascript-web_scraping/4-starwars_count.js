#!/usr/bin/node

const request = require('request');

const id = 18;
const urlPeople = 'https://swapi-api.alx-tools.com/api/people';
const urlId = urlPeople + '/' + id + '/';
request(urlId, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    const jsonData = JSON.stringify(response);
    const jsonNew = JSON.parse(jsonData);
    const jsonBody = JSON.parse(jsonNew.body);
    console.log((jsonBody.films.length));
  }
});
