#!/usr/bin/node
const phrases = 'C is fun';
const num = process.argv[2];
let i = 0;
if (parseInt(num)) {
  while (i < num) {
    console.log(phrases);
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
