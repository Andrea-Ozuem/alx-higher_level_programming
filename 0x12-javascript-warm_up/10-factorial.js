#!/usr/bin/node

function fac (n) {
  if (isNaN(n)) return 1;
  return n < 2 ? 1 : n * fac(n - 1);
}
const num = parseInt(process.argv[2]);
console.log(fac(num));
