#!/usr/bin/node
const fs = require('fs');
// a script that writes a string to a file.
// it write the content of the file in utf-8.

const FileName = process.argv[2];
const TextToWrite = process.argv[3];

fs.writeFile(FileName, TextToWrite, 'utf-8', err => {
  if (err) {
    console.log(err);
  }
});
