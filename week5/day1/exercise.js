// Exercise 1: compareToTen function
function compareToTen(num) {
    return new Promise((resolve, reject) => {
      if (num <= 10) {
        resolve("The number is less than or equal to 10.");
      } else {
        reject("The number is greater than 10.");
      }
    });
  }
  
  // Test for Exercise 1
  compareToTen(15)
    .then(result => console.log(result))
    .catch(error => console.log(error));
  
  compareToTen(8)
    .then(result => console.log(result))
    .catch(error => console.log(error));
  
  // Exercise 2: Promise that resolves after 4 seconds
  const successPromise = new Promise((resolve) => {
    setTimeout(() => {
      resolve("success");
    }, 4000);
  });
  
  // Testing the promise for Exercise 2
  successPromise.then(result => console.log(result));
  
  // Exercise 3: Using Promise.resolve and Promise.reject
  const resolvedPromise = Promise.resolve(3);
  resolvedPromise.then(value => console.log(value));
  
  const rejectedPromise = Promise.reject("Boo!");
  rejectedPromise.catch(error => console.log(error));
  