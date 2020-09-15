#!/usr/bin/node
const factorial = function fac (n) {
  const number = n < 2 ? 1 : n * fac(n - 1);
  if (isNaN(number)) {
    return 1;
  } else {
    return number;
  }
};

console.log(factorial(process.argv[2]));
