#!/usr/bin/node

let num = parseInt(process.argv[2]);
if (num) {
  for (; num > 0; num--) console.log('C is fun');
} else console.log('Missing number of occurrences');
