#!/usr/bin/node
//a script that prints the addition of 2 integers
function add(a, b) {
  return a + b;
}
const args = process.argv;
const argNum1 = parseInt(args[2]);
const argNum2 = parseInt(args[2]);
console.log(add(argNum1,argNum2));
