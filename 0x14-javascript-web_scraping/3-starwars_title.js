#!/usr/bin/node

const request = require('request');

try {
  const url = 'https://swapi-api.hbtn.io/api/films';
  request(url, (error, response, body) => {
    if (error) throw error;
    const obj = JSON.parse(body);
    console.log(obj.results[process.argv[2] - 1].title);
  });
} catch (error) {
  console.log(error);
}
