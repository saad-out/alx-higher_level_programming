#!/usr/bin/node
const size = parseInt(require('process').argv[2]);
if (size) {
  let x = 'X';
  for (let i = 1; i < size; i++) {
    x += 'X';
  }
  for (let i = 0; i < size; i++) {
    console.log(x);
  }
} else {
  console.log('Missing size');
}
