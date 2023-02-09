#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error == null) {
    const myObj = {};
    const obj = JSON.parse(body);
    for (let i = 0; i < obj.length; i++) {
      if (obj[i].completed === true) {
        if (myObj[obj[i].userId] === undefined) {
          myObj[obj[i].userId] = 0;
        }
        myObj[obj[i].userId] += 1;
      }
    }
    console.log(myObj);
  }
});
