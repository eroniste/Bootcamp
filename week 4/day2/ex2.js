const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

colors.forEach((color, index) => {
    let suffix = index === 0 ? "st" : index === 1 ? "nd" : index === 2 ? "rd" : "th";
    console.log(`${index + 1}${suffix} choice is ${color}.`);
});
