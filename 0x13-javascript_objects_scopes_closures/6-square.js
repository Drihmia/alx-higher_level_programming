#!/usr/bin/node
const pSquare = require('./5-square');
module.exports = class Square extends pSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    if (this.height) {
      let str = c.repeat(this.height);
      str += ('\n');
      str = str.repeat(this.height);
      console.log(str.slice(0, -1));
    }
  }
};
