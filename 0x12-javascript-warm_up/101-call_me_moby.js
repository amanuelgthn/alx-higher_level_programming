#!/usr/bin/node
// function tha executes x times a function
// function must be visible from the outside
exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  while (i < x) {
    theFunction();
    i++;
  }
};
