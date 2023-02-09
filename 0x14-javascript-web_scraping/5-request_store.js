#!/usr/bin/node
const args = require('process').argv;
const request = require('request');
const fs = require('fs');

request(args[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(args[3], body, { encoding: 'utf8' }, err => {
      if (err) console.log(err);
    });
  }
});
