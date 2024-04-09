#!/usr/bin/node

const args = process.argv;

if (typeof (Number(args[2])) !== 'number' || !args[2] || isNaN(args[2])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Number(args[2])}`);
}
