#!/usr/bin/node
// Prints the number of arguments already printed and the new argument value
exports.logMe = function (item) {
  this.times = (this.times || 0) + 1;
  console.log(`${this.times - 1}: ${item}`);
};
