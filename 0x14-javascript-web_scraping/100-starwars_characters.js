#!/usr/bin/node

const request = require('request');

try {
  const url = 'https://swapi-api.hbtn.io/api/films';
  request(url, (error, response, body) => {
    if (error) throw error;
    const obj = JSON.parse(body);
    const cantPersonajes = (obj.results[process.argv[2] - 1].characters).length;
    for (let x = 0; x < cantPersonajes; x++) {
      const url1 = obj.results[process.argv[2] - 1].characters[x];
      request(url1, (error1, response1, body1) => {
        const obj1 = JSON.parse(body1);
        console.log(obj1.name);
      });
    }
  });
} catch (error) {
  console.log(error);
}
