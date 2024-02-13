#!/usr/bin/node
const dict = require('./101-data').dict;

const dic = {};
for (const key in dict) {
  const value = dict[key];
  if (!(value in dic)) {
    dic[value] = [key];
  } else {
    const listKey = dic[value];
    listKey[listKey.length] = key;
  }
}
console.log(dic);
