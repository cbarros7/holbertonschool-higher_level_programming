#!/usr/bin/node
let response;
if (process.argv.length < 3) {
  response = 'No argument';
} else if (process.argv.length === 3) {
  response = 'Argument found';
} else {
  response = 'Argument found';
}
console.log(response);
