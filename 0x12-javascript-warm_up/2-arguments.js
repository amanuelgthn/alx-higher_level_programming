#!/usr/bin/node
// script that prints a message depending of the number of arguments passed
const args = process.argv;
if (args.length > 3) {
  console.log('Arguments found');
} else if (args.length == 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
