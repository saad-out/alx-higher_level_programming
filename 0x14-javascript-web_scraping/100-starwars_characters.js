#!/usr/bin/node
const args = require('process').argv;
const request = require('request');

const movie = `https://swapi-api.alx-tools.com/api/films/${args[2]}/`;
request(movie, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  body = JSON.parse(body);
  for (const character of body.characters) {
    request(character, (err, res, body) => {
      if (err) {
        console.log(err);
        return;
      }

      body = JSON.parse(body);
      console.log(body.name);
    });
  }
});
