#!/usr/bin/node
// A JS that reads and prints the content of a file.
const process = require('process');
const filesystem = require('fs');

const file = process.argv[2];

filesystem.readFile(file, 'utf8', function (err, data) {
  if (err != null) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
