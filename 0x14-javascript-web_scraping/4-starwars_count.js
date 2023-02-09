#!/usr/bin/node
const args = require('process').argv;
const request = require('request');

request(args[2], (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  body = JSON.parse(body);
  const wedgeAntilles = 'https://swapi-api.alx-tools.com/api/people/18/';
  let count = 0;
  for (const movie of body.results) {
    if (movie.characters.includes(wedgeAntilles)) count++;
  }
  console.log(count);
});
