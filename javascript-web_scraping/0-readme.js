#!/usr/bin/node
const theFile = process.argv[2];
const fs = require( 'fs' );
fs.readFile(theFile, 'utf8', (err, data) => {
    if (err) {
        console.log(err);
    } else {
        theFile = data;
        console.log(theFile);
    }
});
