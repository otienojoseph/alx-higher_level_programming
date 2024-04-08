#!/usr/bin/node

const args = process.argv.slice(2);
const argsInt = args.map(a => parseInt(a));

function secondBiggest (a) {
  // come back to this to optimize
  const b = a.sort();
  return b.at(-2);
}

console.log(secondBiggest(argsInt));
