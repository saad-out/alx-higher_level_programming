#!/usr/bin/node
const args = require('process').argv;
const request = require('request');

const completedTasks = {};
for (let i = 1; i <= 10; i++) {
  completedTasks[i] = 0;
}

const url = String(args[2]);
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  body = JSON.parse(body);
  for (const task of body) {
    if (task.completed) completedTasks[task.userId]++;
  }

  console.log(completedTasks);
});
