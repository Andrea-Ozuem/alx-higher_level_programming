#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) throw error;
  const chars = JSON.parse(body).characters;
  for (const char of chars) {
    request(char, (error, response, body) => {
      if (error) throw error;
      console.log(JSON.parse(body).name);
    });
  }
});
