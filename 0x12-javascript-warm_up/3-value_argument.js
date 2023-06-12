#!/usr/bin/node
// script that prints the first argument passed to it
const args = process.argv;
if (args.length < 3) {
  console.log('No argument');
} else if (args.length === 3) {
  console.log(args[2]);
}
