import { people } from './data.js';
function calculateAverageAge(persons) {
    const total = persons.reduce((sum, person) => sum + person.age, 0);
    const average = total / persons.length;
    console.log("Average Age:", average);
}
calculateAverageAge(people);