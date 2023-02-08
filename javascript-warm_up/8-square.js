#!/usr/bin/node
const size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
} else {
<<<<<<< HEAD
  for (leti = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
=======
    for (let i =0; i < size; i++) {
        console.log('X'.repeat(size));
    }
}
>>>>>>> 8e118ce800d505b58f872af20c70be77f00950f7
