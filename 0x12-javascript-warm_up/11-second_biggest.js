#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const list = process.argv.slice(2).sort((a, b) => b - a);
  console.log(list[1]);
}
