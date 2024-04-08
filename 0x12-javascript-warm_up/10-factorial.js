#!/usr/bin/node

const args = process.argv;

const factorial = (a) => {
  const b = Number(a);
  if (b < 1 || isNaN(b)) {
    return 1;
  }
  return b * factorial(b - 1);
};

console.log(factorial(args[2]));
