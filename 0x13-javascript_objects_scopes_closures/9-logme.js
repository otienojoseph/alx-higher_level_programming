#!/usr/bin/node

let count = 0;
exports.logMe = function (item) {
  if (item) {
    count = count + 1;
  }
  console.log(`${count - 1}: ${item}`);
};
