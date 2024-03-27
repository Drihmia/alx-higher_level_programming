#!/usr/bin/node
const req = require('request');
// a script that display the status code of a GET request.
// The status code will be printed like this: code: <status code>.
// I must use request module.

const url = process.argv[2];

req(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    if (response.statusCode !== 200) {
      process.exit(1);
    }
    const results = JSON.parse(body).results;
    // console.log(results);

    let counter = 0;

    results.forEach(episode => {
      const charPerEpisode = episode.characters;

      charPerEpisode.forEach(link => {
        if (link.includes('18')) {
          counter++;
        }
      });
    });
    console.log(counter);
  }
});
