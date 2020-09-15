#!/usr/bin/node
let num_ = Number(process.argv[2]);

if (parseInt(num_)) {
  console.log('My number is: ' + process.argv[2]);
} else {
  console.log('Not a number');
}
