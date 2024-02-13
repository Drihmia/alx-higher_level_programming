#!/usr/bin/node

const args = process.argv.slice(2);

if (args[0] === undefined || args[1] === undefined) {
  console.log(0);
} else {
  // I ve used the spread operator "..."
  let maxVal = Math.max(...args);

  const array = args.filter(num => +num !== maxVal);

  maxVal = Math.max(...array);
  console.log(maxVal);
}
