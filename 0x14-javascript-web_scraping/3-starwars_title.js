#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`

request (url, function (error, response, body) {
  console.log(JSON.parse(body).title);
});
