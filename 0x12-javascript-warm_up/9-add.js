#!/usr/bin/node

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

function add (a, b) {
  return a + b;
}

if (process.argv.length < 4) {
  console.log(NaN);
} else {
  console.log(add(num1, num2));
}
