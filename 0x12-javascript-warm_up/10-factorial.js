#!/usr/bin/node

const arg = Number(process.argv[2]);

/* n! = n * (n-1)! */
function factorial (n) {
  if (n < 1) { return 1; }

  return n * factorial(n - 1);
}

if (!arg) {
  console.log(NaN);
} else {
  console.log(factorial(arg));
}
