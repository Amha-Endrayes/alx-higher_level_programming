#!/usr/bin/node
const { argv } = require('node:process');

if (argv[2] === undefined) {
  console.log('No Arguments');
} else {
  console.log(argv[2]);
}
