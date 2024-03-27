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
    const results = await JSON.parse(body).results;
    // console.log(results);

    let charLink;
    results.some(episode => {
      charLink = episode.characters.find(string => string.includes('18'));
      if (charLink) {
        return charLink;
      }
      return false;
    });
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
