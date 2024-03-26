#!/usr/bin/node
const req = require('request');
// a script that display the status code of a GET request.
// The status code will be printed like this: code: <status code>.
// I must use request module.

const url = process.argv[2];

req(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  try {
    const charName = JSON.parse(body).results[0].characters;
    const charLink = charName.find(string => string.includes('18'));
    req(charLink, (err, response, body) => {
      if (err) {
        console.log(err);
      }
      try {
        console.log(JSON.parse(body).films.length);
      } catch (parseError) {
        console.error(parseError);
      }
    });
  } catch (parseError) {
    console.error(parseError);
  }
});
