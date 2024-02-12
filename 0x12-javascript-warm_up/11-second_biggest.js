#!/usr/bin/node

const args = process.argv.slice(2);

const numbers = args.map(Number).filter(num => Number.isInteger(num));

if (numbers.length < 2) {
  console.log(0);
} else {
  numbers.sort((a, b) => b - a);
  const secondBiggest = numbers[1];

  console.log(secondBiggest);
}
