#!/usr/bin/node
// Script that prints a square
// The first argument is the size of the square
// If the first argument can’t be converted to an integer, print “Missing size”
// You must use the character X to print the square
// You must use console.log(...) to print all output
// You are not allowed to use var
// You must use a loop (while, for, etc.)
const args = process.argv;
const argNum = parseInt(args[2]);
let i = 0;
let j = 0;
if (isNaN(argNum)) {
  console.log('Missing size');
} else {
  while (i < argNum) {
    for (j = 0; j < argNum; i++) {
      process.stdout.write('#');
    }
    consol.log();
    i++;
  }
}
