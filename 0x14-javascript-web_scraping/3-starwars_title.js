#!/usr/bin/node

const search = process.argv[2];
const url = 'http://swapi.co/api/films/' + search;
const request = require('request');
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const title = JSON.parse(body).title;
  console.log(title);
});
