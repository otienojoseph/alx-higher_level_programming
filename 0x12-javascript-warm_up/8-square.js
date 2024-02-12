#!/usr/bin/node

const argCount = process.argv[2];

for (let i = 0; i < argCount; i++) {
  let line = '';
  for (let j = 0; j < argCount; j++) {
    line += 'x';
  }
  console.log(line);
}
