#!/usr/bin/node

if (process.argv[2]) {
  const num = parseInt(process.argv[2]);
  if (num) console.log(`My number: ${num}`);
  else console.log('Not a number');
} else {
  console.log('Not a number');
}
