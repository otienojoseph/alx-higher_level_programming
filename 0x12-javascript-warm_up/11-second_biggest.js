#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

function secondBiggest (a) {
  if (a.length <= 1) {
    return 0;
  }

  let largest = args[0];
  let secondLargest = args[1];

  for (let i = 0; i < args.length; i++) {
    if (args[i] > largest) {
      secondLargest = largest;
      largest = args[i];
    } else if (args[i] > secondLargest && args[i] !== largest) {
      secondLargest = args[i];
    }
  }
  return secondLargest;
}

console.log(secondBiggest(args));
