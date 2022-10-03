#!/usr/bin/node
const argv = process.argv;
if (argv[2] === undefined) {
  console.log('No Arguments');
} else {
  console.log(argv[2]);
}
