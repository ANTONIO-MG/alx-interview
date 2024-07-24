#!/usr/bin/node
// This module iterates over the Star Wars API

const request = require('request');
const { promisify } = require('util');

const requestAsync = promisify(request);

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

async function getFilmData () {
  try {
    const response = await requestAsync(url);
    const data = JSON.parse(response.body);

    for (const person of data.characters) {
      const personResponse = await requestAsync(person);
      const personData = JSON.parse(personResponse.body);
      console.log(personData.name);
    }
  } catch (error) {
    console.error('Error making request:', error);
  }
}

getFilmData();
