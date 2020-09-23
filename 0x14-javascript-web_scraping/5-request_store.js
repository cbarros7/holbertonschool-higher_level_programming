#!/usr/bin/node

const requests = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
requests.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(file, body, 'utf8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
