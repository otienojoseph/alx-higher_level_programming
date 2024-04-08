#!/usr/bin/node

const args = process.argv.slice(2);
const argsInt = args.map(a => parseInt(a));

function secondBiggest (a) {
  if (a.length <= 1) {
    return 0;
  }

  // Optimized version
  const sortedArr = a.toSorted((a, b) => a - b);
  return sortedArr.at(-2);

  // manual iteration
  // let temp;
  // for (let i = 0; i < a.length - 1; i++) {
  //     for (let j = 0; j < a.length - 1 - i; j++) {
  //         if (a[j] > a[j + 1]) {
  //             temp = a[j];
  //             a[j] = a[j + 1];
  //             a[j + 1] = temp;
  //
  //         }
  //     }
  // }
  // return a.at(-2);
}

console.log(secondBiggest(argsInt));
