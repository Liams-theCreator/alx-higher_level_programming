#!/usr/bin/node
argu = process.argv[2];

if (!parseInt(argu)) {
  console.log('Not a number');
} else {
  console.log(parseInt(argu));
}
