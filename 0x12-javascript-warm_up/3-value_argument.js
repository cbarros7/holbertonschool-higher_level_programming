#!/usr/bin/node
let str;
if (process.argv.length < 3) {
  str = 'No argument';
} else {
  str = process.argv[2];
}
console.log(str);
