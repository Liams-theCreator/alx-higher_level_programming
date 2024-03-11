#!/usr/bin/node
const Argu = parseInt(process.argv[2]);

function factorial (number) {
  if (number === 1 || !number) {
    return (1);
  }
  return (number * factorial(number - 1));
}

console.log(factorial(Argu));
