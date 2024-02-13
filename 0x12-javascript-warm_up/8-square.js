#!/usr/bin/node
// I ve used the while loop in this example.

const str = 'x';
const args = process.argv;
const arg2 = args[2];

// if no argument is passed or is not convertable into
// a integer, print Missing size.
if (arg2 !== undefined && !isNaN(1 * arg2)) {
  let i = 0;
  while (i < arg2) {
    console.log(str.repeat(arg2));
    i++;
  }
} else {
  console.log('Missing size');
}
