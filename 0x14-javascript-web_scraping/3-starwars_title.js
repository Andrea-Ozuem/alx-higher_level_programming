#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(url).on('response', (response) => {
  console.log(JSON.parse(response).title);
});
