const { readFile, writeFile } = require('./fileManager');
const content = readFile('Hello World.txt');
console.log("Content read:", content);
writeFile('Bye World.txt', 'Writing to the file');