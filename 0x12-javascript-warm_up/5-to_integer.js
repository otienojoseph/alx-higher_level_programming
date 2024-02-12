#!/usr/bin/node

const arg = process.argv[2];

console.log(`${Number(arg) ? `My number: ${Math.floor(Number(arg))}` : 'Not a number'}`);
