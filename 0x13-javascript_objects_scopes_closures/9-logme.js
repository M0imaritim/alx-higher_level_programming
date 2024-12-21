#!/usr/bin/node
let newarg = 0;

exports.logMe = function (item) {
  console.log(newarg + ': ' + item);
  newarg++;
};
