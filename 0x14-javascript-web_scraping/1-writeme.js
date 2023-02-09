#!/usr/bin/node
const args = require('process').argv;
const fs = require('fs');

if (args[2] && args[3]) {
  fs.writeFile(args[2], args[3], err => {
    if (err) console.log(err);
  });
}
