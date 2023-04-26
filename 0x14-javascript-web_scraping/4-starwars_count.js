#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const charUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, function (error, response, body) {
  if (error) throw error;
  const results = JSON.parse(body).results;

  const filtered = results.filter(res =>
    res.characters.includes(charUrl));
  console.log(filtered.length);
});
