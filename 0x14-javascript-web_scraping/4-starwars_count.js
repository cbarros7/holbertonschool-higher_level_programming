#!/usr/bin/node

const requests = require('request');
const url = process.argv[2];

requests(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const results = JSON.parse(body).results;
  let counter = 0;
  for (const lists of results) {
    for (const characters of lists.characters) {
      if (characters.includes('18')) {
        counter = counter + 1;
      }
    }
  }
  console.log(counter);
});
