#!/usr/bin/node
const lista = [];
for (let i = 2; i < process.argv.length; i++) {
  lista.push(process.argv[i]);
}
if (process.argv.length < 4) {
  console.log(0);
} else {
  console.log(Number(lista.sort().slice(-2)[0]));
}
