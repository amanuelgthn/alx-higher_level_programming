#!/usr/bin/node
// function that increments and calls a function.
// function must be visible from outside
exports.addMeMaybe = function (number, theFunction) {
  number = number + 1;
  theFunction(number);
};
