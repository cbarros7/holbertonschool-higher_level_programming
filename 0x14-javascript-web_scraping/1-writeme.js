#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const toWrite = process.argv[3];
fs.writeFile(file, toWrite, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
