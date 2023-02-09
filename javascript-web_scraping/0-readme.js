#!/usr/bin/node
const aFile = process.argv[2];
const fs = require( 'fs' );
fs.readFile(aFile, 'utf8', (err, data) => {
    if (err) {
        console.log(err);
    } else {
        aFile = data;
        console.log(aFile);
    }
});
