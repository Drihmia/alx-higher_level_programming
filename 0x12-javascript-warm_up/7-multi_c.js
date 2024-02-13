#!/usr/bin/env node
// I ve used the for loop in this example.

const str = 'C is fun';
const args = process.argv;
const arg2 = args[2];

if (arg2 !== undefined && !isNaN(1 * arg2)) {
  for (let i = 0; i < arg2; i++) {
    console.log(str);
  }
} else {
  console.log('Missing number of occurrences');
}
