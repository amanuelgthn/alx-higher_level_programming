#!/usr/bin/node
//a script that prints the addition of 2 integers
function add(a, b) {
  return a + b;
}
const args = process.argv;
let argNum1 = Number(args[2]);
let argNum2 = Number(args[3]);
let result = add(argNum1, argNum2);
console.log(result);
