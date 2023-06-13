#!/usr/bin/node
// script that prints x times "C is fun"
// Where x is the first argument of the script
// If the first argument can’t be converted to an integer, print “Missing number of occurrences”
// You must use console.log(...) to print all output
// You are not allowed to use var
// You can use only two console.log
// You must use a loop (while, for, etc.)
const args = process.argv;
const argNum = parseInt(args[2]);
let i = 0;
if (isNaN(argNum)) {
  console.log('Missing number of occurrences');
} else {
  while (i < argNum) {
    console.log('C is fun');
    i++;
  }
}
