#!/usr/bin/node
// starwars characters

const request = require('request');
const process = require('process');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

const makerequest = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const response = JSON.parse(body);
        console.log(response.name);
        resolve(response);
      }
    });
  });
};

const getmovie = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const response = JSON.parse(body);
        resolve(response);
      }
    });
  });
};

async function getcharacter (url) {
  const response = await getmovie(url);
  for (const items of response.characters) {
    await makerequest(items);
  }
}

getcharacter(url);
