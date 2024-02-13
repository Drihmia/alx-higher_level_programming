#!/usr/bin/node
const pSquare = require('./5-square');
module.exports = class Square extends pSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    if (this.size) {
      let str = 'X'.repeat(this.size);
      str += ('\n');
      str = str.repeat(this.size);
      console.log(str.slice(0, -1));
    }
  }
};
