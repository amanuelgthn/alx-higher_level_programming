#!/usr/bin/node
// function that prints the number of already printed and the new argument value
// Output format: <number of arguments already printed>: <current argument value>
let count = 0;
exports.logme = function (item) {
  count += 1;
  console.log('%d: %s', count, item);
};
