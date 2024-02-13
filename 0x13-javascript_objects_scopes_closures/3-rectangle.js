#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w && h && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      let str = 'X'.repeat(this.width);
      str += ('\n');
      str = str.repeat(this.height);
      console.log(str.slice(0, -1));
    }
  }
};
