#!/usr/bin/node
const args = require('process').argv;
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + String(args[2]);
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
