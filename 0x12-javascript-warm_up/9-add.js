#!/usr/bin/node

function add(a, b) {
    return a + b;
}

const argu1 = parseInt(process.argv[2]);
const argu2 = parseInt(process.argv[3]);

console.log(add(argu1, argu2));