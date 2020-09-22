#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf8', function read (err, data) {
  if (err) {
    console.log(err);
    return;
  }
  const content = data;
  console.log(content);
});
