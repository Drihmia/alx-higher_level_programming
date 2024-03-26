#!/usr/bin/node
const fs = require('fs');
// a script that reads and prints the content of a file.
// it reads the content of the file in utf-8.

const filename = process.argv[2];

fs.readFile(filename, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
