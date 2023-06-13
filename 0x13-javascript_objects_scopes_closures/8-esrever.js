#!/usr/bin/node
// write a function that returns the number of occurrences in a list
exports.esrever = function (list) {
    let arr = []
    const lenList = list.length;
    let i = 0;
    while (i < lenList + 1) {
        arr[i] = list[lenList - i]
      i++;
    }
    return arr;
  };