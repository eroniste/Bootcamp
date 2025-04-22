const _ = require('lodash');
const { add, multiply } = require('./math');
console.log("Add:", add(2, 3));
console.log("Multiply:", multiply(4, 5));
console.log("Lodash chunk:", _.chunk([1,2,3,4,5], 2));