#!/usr/bin/node
const lista = [];
for (let i = 2; i < process.argv.length; i++) {
  const number = parseInt(process.argv[i]);
  lista.push(number);
}
if (lista.length < 2) {
  console.log(0);
} else {
  console.log(lista.sort().slice(-2)[0]);
}
