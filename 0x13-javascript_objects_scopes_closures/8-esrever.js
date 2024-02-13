#!/usr/bin/node

exports.esrever = function (list) {
  const lastIndex = list.length - 1;
  let temp;
  for (let i = 0; i <= lastIndex / 2; i++) {
    temp = list[lastIndex - i];
    list[lastIndex - i] = list[i];
    list[i] = temp;
  }
  return list;
};
