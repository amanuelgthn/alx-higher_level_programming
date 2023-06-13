#!/usr/bin/node
// a script that prints the addition of 2 integers
function add (a, b) {
  return a + b;
}
const args = process.argv;
const argNum1 = Number(args[2]);
const argNum2 = Number(args[3]);
const result = add(argNum1, argNum2);
console.log(result);
