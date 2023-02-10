#!/usr/bin/node
const args = require('process').argv;
const request = require('request');

async function displayCharacters (id) {
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${id}/`;

  // Get movie
  let movie = await new Promise((resolve, reject) => {
    request(movieUrl, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
  movie = JSON.parse(movie);

  // Display every character in movie
  for (const characterUrl of movie.characters) {
    // Get character
    let character = await new Promise((resolve, reject) => {
      request(characterUrl, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(body);
        }
      });
    });
    character = JSON.parse(character);

    // Log character
    console.log(character.name);
  }
}

displayCharacters(args[2]);
