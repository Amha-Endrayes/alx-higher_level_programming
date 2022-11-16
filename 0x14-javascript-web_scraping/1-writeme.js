#!/usr/bin/node
// A JS that writes a string to a file
const fs = require('fs');
const argstr = process.argv[3];
fs.writeFile(process.argv[2], argstr, function (err, argstr) {
  if (err) {
    console.log(err);
  }
});
