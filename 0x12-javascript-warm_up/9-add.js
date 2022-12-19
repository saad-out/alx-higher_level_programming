#!/usr/bin/node
function add (a, b) {
  if (Number.isInteger(a) && Number.isInteger(b)) {
    return (a + b);
  } else {
    return (NaN);
  }
}

const args = require('process').argv;
const n1 = parseInt(args[2]);
const n2 = parseInt(args[3]);

console.log(add(n1, n2));
