#!/usr/bin/node

const argCount = Number(process.argv[2]);

if (argCount) {
  for (let i = 0; i < argCount; i++) {
    let line = '';
    for (let j = 0; j < argCount; j++) {
      line += 'x';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
