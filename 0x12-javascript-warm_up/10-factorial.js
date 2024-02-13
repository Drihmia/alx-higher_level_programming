#!/usr/bin/env node

function factorial (number) {
  const fact = 1;

  if (number === undefined) {
    return fact;
  }

  if (number <= 0) {
    return fact;
  }

  return number-- * factorial(number);
}

const fac = factorial(process.argv[2]);
console.log(fac);
