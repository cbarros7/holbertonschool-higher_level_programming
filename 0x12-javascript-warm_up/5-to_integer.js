#!/usr/bin/node
const num_ = parseInt(process.argv[2]);

if (isNaN(num_)) {
  console.log('Not a number');
} else {
  console.log('My number is: ' + num_);
}
