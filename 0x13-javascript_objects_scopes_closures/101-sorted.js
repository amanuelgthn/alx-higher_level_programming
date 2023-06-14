#!/usr/bin/node
// A script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence
// import dict from the file 101-data.js
// print the new dictionary at the end
const dict = require('./101-data.js').dict;
const key = Object.keys(dictionary);
const value = Object.values(dictionary);
