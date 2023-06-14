#!/usr/bin/node
// Write a function that converts a number from base 10 to another base passed as argument
// Declaring any variable (var, let) not allowed
// importing any file not allowed 
exports.converter = function (base) {
  return num => num.toString(base);
  };
