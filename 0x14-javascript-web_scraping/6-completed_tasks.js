#!/usr/bin/node
// A JS that computes the number of tasks completed by user id
require('request').get(process.argv[2], function (err, r, body) {
  if (err) {
    console.log(err);
  } else {
    const res = {};
    const temp = JSON.parse(body);
    for (let i = 0; i < temp.length; i++) {
      if (temp[i].completed) {
        if (!(temp[i].userId in res)) {
          res[temp[i].userId] = 0;
        }
        res[temp[i].userId] += 1;
      }
    }
    console.log(res);
  }
});
