#!/usr/bin/node
// Script that imports an array and computes a new array
// Must use a Map
// A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
// Print both the initial list and the new list
const list = require('./100-data.js').list;
const newData = list.map((x, index) => x * index);
console.log(list);
console.log(newData);
