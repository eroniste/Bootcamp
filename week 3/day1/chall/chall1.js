

let sentence = "This dinner is not that bad ! You cook well";
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");

if (wordNot < wordBad && wordNot !== -1 && wordBad !== -1) {
    sentence = sentence.substring(0, wordNot) + "good" + sentence.substring(wordBad + 3);
}
console.log(sentence);
