#!/usr/bin/node
const fs = require('fs');

const writeToFile = (filePath, content) => {
  fs.writeFile(filePath, content, 'utf8', (err) => {
    if (err) {
      console.error(`An error occurred: ${err}`);
    } else {
      console.log(`Successfully wrote to ${filePath}`);
    }
  });
};

if (process.argv.length !== 4) {
  console.log('Usage: node script.js <file_path> <string_to_write>');
} else {
  const filePath = process.argv[2];
  const content = process.argv[3];
  writeToFile(filePath, content);
}
