#!/usr/bin/node
function factorial (n) {
  if (!Number.isInteger(n) || n === 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

const n = parseInt(require('process').argv[2]);

console.log(factorial(n));
