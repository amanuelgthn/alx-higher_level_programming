#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const filePath = process.argv[3];
const url = process.argv[2];
request(url, (err, response) => {
    if (err) {
        console.log(err);
    } else {
        const jsonData = JSON.stringify(response);
        const jsonNew = JSON.parse(jsonData);
        fs.writeFile(filePath, jsonNew.body, 'utf8', (err) => {
            if (err) throw err;
        });
    }
});
