#!/usr/bin/node
const num_ = parseInt(process.argv[2]);

if (num_) {
  console.log('My number is: ' + num_);
} else {
  console.log('Not a number');
}
