let number = prompt("Please enter a number:");

while (typeof number !== "number" || number < 10) {
  number = prompt("Please enter a number greater than or equal to 10:");
}
