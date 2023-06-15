#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
let x = myObject.value;
myObject.incr = function () {
  x = x + 1;
  myObject.value = x;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
