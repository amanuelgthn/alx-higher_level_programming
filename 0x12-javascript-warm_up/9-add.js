#!/usr/bin/node
//a script that prints the addition of 2 integers
function add(a, b) {
  return a + b;
}
const args = process.argv;
let argNum1 = parseInt(args[2]);
let argNum2 = parseInt(args[2]);
let result = add.call(this, argNum1, argNum2);
console.log(result);