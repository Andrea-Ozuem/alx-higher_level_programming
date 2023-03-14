#!/usr/bin/node

const num = parseInt(process.argv[2]);
if (num) {
  for (let i = num; i > 0; i--) {
    console.log('X'.repeat(num));
  }
} else console.log('Missing size');
