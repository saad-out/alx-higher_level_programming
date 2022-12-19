#!/usr/bin/node
const args = require('process').argv;

let max;
let maxSecond;
let tmp;

if (args.length > 3) {
  max = parseInt(args[2]);
  for (let i = 2; i < args.length; i++) {
    tmp = parseInt(args[i]);
    if (max < tmp) {
      max = tmp;
    }
  }

  maxSecond = parseInt(args[2]);
  for (let i = 2; i < args.length; i++) {
    tmp = parseInt(args[i]);
    if (maxSecond < tmp && tmp !== max) {
      maxSecond = tmp;
    }
  }
} else {
  maxSecond = 0;
}

console.log(maxSecond);
