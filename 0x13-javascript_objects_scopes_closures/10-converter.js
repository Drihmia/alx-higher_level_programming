#!/usr/bin/node
exports.converter = function (base) {
  function inner (num) {
    return num.toString(base);
  }
  return inner;
};
