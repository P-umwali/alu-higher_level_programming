#!/usr/bin/node
const firstArgv = process.argv[2];
if (isNaN(firstArgv)) {
    console.log('Missing number of occurences');
} else{
    for (let i = 0; i< firstArgv; i++){
        console.log('C is fun');
    }
}
