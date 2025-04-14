// 🌟 Exercise 4 : Person Class
class Person {
    constructor(name) {
      this.name = name;
    }
  }
  
  const member = new Person('John');
  console.log('Exercise 4 Output:', typeof member); // Output: 'object'
  
  // 🌟 Exercise 5 : Dog Class
  class Dog {
    constructor(name) {
      this.name = name;
    }
  }
  
  // ✅ Correct Version - Option 2
  class Labrador extends Dog {
    constructor(name, size) {
      super(name); // Call the parent constructor
      this.size = size;
    }
  }
  
  const lab = new Labrador('Buddy', 'Large');
  console.log('Exercise 5 Output:', lab.name, lab.size); // Output: 'Buddy Large'
  
  // 🌟 Exercise 6 : Challenges
  
  // Part 1: Evaluate expressions
  console.log('Exercise 6 - Part 1:');
  console.log('[2] === [2] ->', [2] === [2]); // false
  console.log('{} === {} ->', {} === {});   // false
  
  // Part 2: Object reference example
  const object1 = { number: 5 }; 
  const object2 = object1; 
  const object3 = object2; 
  const object4 = { number: 5 };
  
  object1.number = 4;
  
  console.log('Exercise 6 - Part 2:');
  console.log('object2.number ->', object2.number); // 4
  console.log('object3.number ->', object3.number); // 4
  console.log('object4.number ->', object4.number); // 5
  
  // Part 3: Animal & Mammal classes
  class Animal {
    constructor(name, type, color) {
      this.name = name;
      this.type = type;
      this.color = color;
    }
  }
  
  class Mammal extends Animal {
    sound(soundMade) {
      return `${soundMade} I'm a ${this.type}, named ${this.name} and I'm ${this.color}`;
    }
  }
  
  const farmerCow = new Mammal('Lily', 'cow', 'brown and white');
  console.log('Exercise 6 - Part 3 Output:', farmerCow.sound('Moooo'));
  // Output: Moooo I'm a cow, named Lily and I'm brown and white
  