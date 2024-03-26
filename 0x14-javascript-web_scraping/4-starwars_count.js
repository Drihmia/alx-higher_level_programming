#!/usr/bin/node
const req = require('request');
// a script that display the status code of a GET request.
// The status code will be printed like this: code: <status code>.
// I must use request module.

const url = process.argv[2];

req(url, async (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const charName = await JSON.parse(body).results[0].characters;
    const charLink = charName.find(string => string.includes('18'));
    if (response.statusCode === 200) {
      req(charLink, (err, response, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).films.length);
        }
      });
    }
  }
});
