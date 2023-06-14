#!/usr/bin/node
// Script that imports an array and computes a new array
// Must use a Map
// A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
// Print both the initial list and the new list
const data = require('./100-data').data;
const newData = data.map(x => x * x);
console.log(newData);

