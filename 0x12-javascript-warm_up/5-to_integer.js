#!/usr/bin/env node
const args = process.argv;
try {
  if (!isNaN(1 * args[2])) {
    console.log(~~(args[2]));
  } else {
    throw new Error('Not a number');
  }
} catch (error) {
  console.log(error.message);
}
