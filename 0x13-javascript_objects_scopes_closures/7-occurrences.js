#!/usr/bin/node
// number of occurences of element in list
exports.nbOccurences = function (list, element) {
  return list.filter((x) => x === element).length;
};
