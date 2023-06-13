#!/usr/bin/node
// Script that computes and prints a factorial
// the first argument is integer(argument can be cast as integer) used for computing the factorial
// Factorial of NaN is 1
// Using Recursion function
// console.log() to print all output
function printFactorial(num) {
  if (num === NaN)
    return 1;
  
}
numArgs = process.argv;
num = Number(numArgs[2];
