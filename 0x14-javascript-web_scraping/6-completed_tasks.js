#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const jsonList = JSON.parse(body);
    const dictionary = {};
    // console.log(jsonList);
    jsonList.forEach(item => {
      if (item.completed === true) {
        if (item.userId in dictionary) {
          dictionary[item.userId] += 1;
        } else {
          dictionary[item.userId] = 1;
        }
      }
    });
    console.log(dictionary);
  }
});
