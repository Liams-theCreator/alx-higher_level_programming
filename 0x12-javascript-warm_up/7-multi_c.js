#!/usr/bin/node
const argu = process.argv[2];

if (!argu) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i <= argu; i++) {
  console.log('C is fun');
}
