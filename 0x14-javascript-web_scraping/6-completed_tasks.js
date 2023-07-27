#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    const jsonData = JSON.stringify(response);
    const jsonNew = JSON.parse(jsonData);
    const jsonBody = JSON.parse(jsonNew.body);
    let j = 0;
    let i = 0;
    let count = 0;
    const countLog = [];
    while (j < jsonBody.length) {
      if (i !== jsonBody[j].userId) {
        i = jsonBody[j].userId;
        if (count > 0) {
          countLog.push(count);
          if (i === jsonBody[j].userId && jsonBody[j].completed === true) {
            count = 1;
          } else {
            count = 0;
          }
        }
      } else if (jsonBody[j].userId === i && jsonBody[j].completed === true) {
        count += 1;
      }
      j++;
    }
    countLog.push(count);
    i = 1;
    const dictTodos = {};
    while (i < countLog.length + 1) {
      dictTodos[i] = countLog[i - 1];
      i++;
    }
    console.log(dictTodos);
  }
});
