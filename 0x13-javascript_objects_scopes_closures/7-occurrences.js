#!/usr/bin/node
// write a function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  const lenList = list.length;
  let i = 0;
  let count = 0;
  while (i < lenList) {
    if (list[i] === searchElement) {
      count += 1;
    }
    i++;
  }
  return count;
};
