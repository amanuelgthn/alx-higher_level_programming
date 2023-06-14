#!/usr/bin/node
// write a function that returns the number of occurrences in a list
exports.esrever = function (list) {
  const arr = [];
  const lenList = list.length;
  let i = 0;
  while (i < lenList) {
    arr[i] = list[lenList - i - 1];
    i++;
  }
  return arr;
};
