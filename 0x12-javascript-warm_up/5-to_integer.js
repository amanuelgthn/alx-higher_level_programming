#!/usr/bin/node
// script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
// If the argument can’t be converted to an integer, print “Not a number”
// You must use console.log(...) to print all output
// You are not allowed to use var
// You are not allowed to use try/catch

const args = process.argv;
if (args.length < 3 || isNaN(Number(args[2]))) {
  console.log('Not a number');
} else if (typeof Number(args[2]) === 'number') {
  console.log('%s: %d', 'My Number', Number(args[2]));
}
