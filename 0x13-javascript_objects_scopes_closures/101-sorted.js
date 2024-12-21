#!/usr/bin/node
const dict = require('./101-data').dict;
const nnew = {};

Object.keys(dict).forEach(function (key, index) {
  if (nnew[dict[key]] === undefined) {
    nnew[dict[key]] = [];
  }
  nnew[dict[key]].push(key);
});

console.log(nnew);
