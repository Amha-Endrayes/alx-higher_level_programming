#!/usr/bin/node
// A JS that prints the title of a Star Wars movie where the episode number matches a given integer
require('request').get('https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/', function (err, r, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
