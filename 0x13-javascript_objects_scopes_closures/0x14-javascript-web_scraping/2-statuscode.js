#!/usr/bin/node
const req = require('request');
// a script that display the status code of a GET request.
// The status code will be printed like this: code: <status code>.
// I must use request module.

const request = req.get(process.argv[2]);

request.on('response', function OnRequestResponse (response) {
  console.log(`code: ${response.statusCode}`);
});
