const userInput = prompt("Enter several words separated by commas:");
const words = userInput.split(",").map(word => word.trim());
const maxLength = Math.max(...words.map(word => word.length));
const border = "*".repeat(maxLength + 4);

console.log(border);
words.forEach(word => {
    const spaces = " ".repeat(maxLength - word.length);
    console.log(`* ${word}${spaces} *`);
});
console.log(border);
