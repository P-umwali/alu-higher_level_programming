#!/usr/bin/node
const fPath = process.argv[2];
const toWrite = process.argv[3];
const fs = require('fs');
fs.writeFile(fPath, toWrite, 'utf-8', function(err, data) {
    if (err) {
        console.log(err);
    }
});
