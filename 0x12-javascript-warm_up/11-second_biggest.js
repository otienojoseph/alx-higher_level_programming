#!/usr/bin/node

const args = process.argv.slice(2);
const argsInt = args.map(a => parseInt(a));

function secondBiggest (a) {
  if (a.length <= 1) {
    return 0;
  }

  let temp;
  // manual, can be optimized
  for (let i = 0; i < a.length; i++) {
    for (let j = 0; j < a.length; j++) {
      if (j > i) {
        temp = j;
      }
    }
  }
  return a[temp - 1];
}

console.log(secondBiggest(argsInt));
