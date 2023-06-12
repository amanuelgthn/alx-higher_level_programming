#!/usr/bin/node
// script that prints 3 lines by using an array of string and a loop
// The first line: “C is fun”
// The second line: “Python is cool”
// The third line: “JavaScript is amazing”
// You must use console.log(...) to print all output
// You are not allowed to use var
// You are not allowed to use any if/else statement
// You can use only one console.log
// You must use a loop (while, for, etc.)
const arrStr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let i = 0;
while (i < arrStr.length) {
  console.log(arrStr[i]);
  i++;
}
