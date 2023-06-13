#!/usr/bin/node
// Script that computes and prints a factorial
// the first argument is integer(argument can be cast as integer) used for computing the factorial
// Factorial of NaN is 1
// Using Recursion function
// console.log() to print all output
function printFactorial (num) {
  if (isNaN(num) || num < 0) {
    return 1;
  }
  if (num === 0) {
    return 1;
  }
  if (num === 1) {
    return 1;
  }
  if (num === 2) {
    return 2;
  }
  return num * printFactorial(num - 1);
}
const numArgs = process.argv;
const num = Number(numArgs[2]);
const ret = printFactorial(num);
console.log(ret);
