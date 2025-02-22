#!/usr/bin/node
const request = require('request');

const API_URL = "https://swapi-api.alx-tools.com/api/films/";
const CHARACTER_ID = "/18/";

function countWedgeMovies() {
    request(API_URL, { json: true }, (error, response, body) => {
        if (error) {
            console.error("Error fetching data:", error.message);
            return;
        }
        
        if (!body.results) {
            console.error("Unexpected response format");
            return;
        }
        
        const count = body.results.filter(film => 
            film.characters.some(charUrl => charUrl.includes(CHARACTER_ID))
        ).length;
        
        console.log(count);
    });
}

countWedgeMovies();

