#!/usr/bin/node
// script that prints the first argument passed to it
const args = process.argv;
if (args[2] == null) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
