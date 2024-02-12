#!/usr/bin/node

const args = process.argv.slice(2);

const numbers = args.map(Number).filter(num => Number.isInteger(num));

if (numbers.length < 2) {
  console.log(0);
} else {
  let max = -Infinity; let result = -Infinity;

  for (const value of numbers) {
    if (value > max) {
      [result, max] = [max, value];
    } else if (value < max && value > result) {
      result = value;
    }
  }

  console.log(result);
}
