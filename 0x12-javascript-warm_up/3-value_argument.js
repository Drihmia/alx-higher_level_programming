#!/usr/bin/node
const args = process.argv;

try {
  if (args[2] !== undefined) {
    console.log(args[2]);
  } else {
    throw new Error('No argument');
  }
} catch (error) {
  console.log(error.message);
}
