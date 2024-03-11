#!/usr/bin/node
const argu = process.argv[2];

if (!parseInt(argu)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(argu));
}
