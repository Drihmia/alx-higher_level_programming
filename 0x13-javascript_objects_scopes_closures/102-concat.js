#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const pathA = './' + args[2];
const pathB = './' + args[3];
const pathC = './' + args[4];

fs.readFile(pathA, 'utf-8', (err, data1) => {
  if (err) {
    return;
  }
  fs.readFile(pathB, 'utf-8', (err, data2) => {
    if (err) {
      return;
    }
    const data3 = (data1 + data2);
    fs.writeFile(pathC, data3, 'utf-8', err => {
      if (err) {
        console.log('Error');
      }
    });
  });
});
