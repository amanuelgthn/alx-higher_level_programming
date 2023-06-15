#!/usr/bin/node
// A script that searches the second biggest integer in the list of arguments
// if no arguments passed print 0
// if the number of arguments is print 0
const args = process.argv;
let i = 2;
const lenArgs = args.length;
const argList = [];
if (lenArgs < 4) {
  console.log(0);
} else {
  for (; i < lenArgs; i++) {
    argList.push(args[i]);
  }
  argList.sort((a, b) => a - b);
  const lenList = argList.length;
  console.log(argList[lenList - 2]);
}
