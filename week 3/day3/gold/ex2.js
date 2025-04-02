
function abbrevName(str) {
    let [firstName, lastName] = str.split(' ');
    return `${firstName} ${lastName[0]}.`;
}

console.log(abbrevName("Robin Singh"));  // "Robin S."
