#!/usr/bin/node

const fs = require('fs');
const request = require('request');

try {
  const url = process.argv[2];
  const filePath = process.argv[3];
  request(url, (error, response, body) => {
    if (error) throw error;
    fs.writeFile(filePath, response.body, 'utf-8', (err) => {
      if (err) throw err;
    });
  });
} catch (error) {
  console.log(error);
}
