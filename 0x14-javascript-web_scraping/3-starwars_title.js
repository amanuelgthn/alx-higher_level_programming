#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const urlId = url + id + '/';
request(urlId, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    const jsonData = JSON.stringify(response);
    const jsonNew = JSON.parse(jsonData);
    const jsonBody = JSON.parse(jsonNew.body);
    console.log(jsonBody.title);
    return (jsonBody.episode_id);
  }
});
