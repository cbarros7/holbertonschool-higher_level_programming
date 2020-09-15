#!/usr/bin/node
const phrases = 'X';
const num = process.argv[2];
if (parseInt(num)) {
  for (let step = 0; step < num; step++) {
    console.log(phrases.repeat(num));
  }
} else {
  console.log('Missing size');
}
