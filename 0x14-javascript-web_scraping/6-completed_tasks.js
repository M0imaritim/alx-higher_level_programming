#!/usr/bin/node
const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);

    // Create an object to store the count of completed tasks for each user
    const completedTasksByUser = {};

    // Loop through the tasks
    tasks.forEach(task => {
      if (task.completed) {
        // If the task is completed, increment the count for the user
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });
    console.log(completedTasksByUser);
  }
});
