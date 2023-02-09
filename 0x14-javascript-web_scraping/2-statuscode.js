#!/usr/bin/node
const args = require('process').argv;
const request = require('request');

request(args[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
