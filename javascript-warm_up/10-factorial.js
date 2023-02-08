#!/usr/bin/node
const argv = parseInt(process.argv[2]);
function factorialize (num) {
  if ((number.isNaN(num)) || (num === 1)) {
    return 1;
  }
  return factorialize(num - 1) * num;
}
console.log(factorialize(argv));
