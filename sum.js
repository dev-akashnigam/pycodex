const prompt = require('prompt-sync')();

function sum(x, y) {
	let sum = parseInt(x) + parseInt(y);
	return sum;
}

let a = prompt("enter first number");
let b = prompt("enter second number");

console.log(sum(a, b));
