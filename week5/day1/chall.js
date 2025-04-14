// 1st Daily Challenge

function makeAllCaps(arr) {
    return new Promise((resolve, reject) => {
      if (arr.every(word => typeof word === 'string')) {
        resolve(arr.map(word => word.toUpperCase()));
      } else {
        reject('All elements must be strings');
      }
    });
  }
  
  function sortWords(arr) {
    return new Promise((resolve, reject) => {
      if (arr.length > 4) {
        resolve(arr.sort());
      } else {
        reject('Array length must be greater than 4');
      }
    });
  }
  
  makeAllCaps([1, "pear", "banana"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result))
    .catch(error => console.log(error));
  
  makeAllCaps(["apple", "pear", "banana"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result))
    .catch(error => console.log(error));
  
  makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
    .catch(error => console.log(error));
  
  // 2nd Daily Challenge
  
  const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`;
  
  function toJs() {
    return new Promise((resolve, reject) => {
      const morseJS = JSON.parse(morse);
      if (Object.keys(morseJS).length === 0) {
        reject('Morse object is empty');
      } else {
        resolve(morseJS);
      }
    });
  }
  
  function toMorse(morseJS) {
    return new Promise((resolve, reject) => {
      const userWord = prompt('Enter a word or sentence:').toLowerCase();
      const morseArray = [];
      
      for (let char of userWord) {
        if (morseJS[char]) {
          morseArray.push(morseJS[char]);
        } else {
          reject(`Character "${char}" not found in morse dictionary`);
          return;
        }
      }
      resolve(morseArray);
    });
  }
  
  function joinWords(morseTranslation) {
    return new Promise((resolve) => {
      const joinedMorse = morseTranslation.join('\n');
      document.body.innerHTML = `<pre>${joinedMorse}</pre>`;
      resolve();
    });
  }
  
  // Chain the functions
  toJs()
    .then(morseJS => toMorse(morseJS))
    .then(morseTranslation => joinWords(morseTranslation))
    .catch(error => console.log(error));
  