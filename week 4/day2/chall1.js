const users = [
    { name: "Ray", course: "Computer Science", isPassed: true },
    { name: "Liam", course: "Computer Science", isPassed: false },
    { name: "Jenner", course: "Information Technology", isPassed: true },
    { name: "Marco", course: "Robotics", isPassed: true },
    { name: "Kimberly", course: "Artificial Intelligence", isPassed: false },
    { name: "Jamie", course: "Big Data", isPassed: false }
  ];
  
  const welcomeStudents = users.map(user => `Hello ${user.name}`);
  console.log(welcomeStudents);
  
  const students = [
    { name: "Ray", course: "Computer Science", isPassed: true },
    { name: "Liam", course: "Computer Science", isPassed: false },
    { name: "Jenner", course: "Information Technology", isPassed: true },
    { name: "Marco", course: "Robotics", isPassed: true },
    { name: "Kimberly", course: "Artificial Intelligence", isPassed: false },
    { name: "Jamie", course: "Big Data", isPassed: false }
  ];
  
  const fullStackResidents = students.filter(student => student.course === 'Computer Science' && student.isPassed);
  console.log(fullStackResidents);
  
  students
    .filter(student => student.isPassed)
    .forEach(student => {
      console.log(`Good job ${student.name}, you passed the course in ${student.course}`);
    });
  
  const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];
  const epicString = epic.reduce((accumulator, currentValue) => {
    return accumulator + ' ' + currentValue;
  }, '');
  console.log(epicString);
  
  const studentsWithRoles = [
    { name: "Ray", lastName: "Smith", role: "Full Stack Resident" },
    { name: "Liam", lastName: "Johnson", role: "Developer" },
    { name: "Jenner", lastName: "Williams", role: "Full Stack Resident" },
    { name: "Marco", lastName: "Brown", role: "Full Stack Resident" }
  ];
  
  const fullStackResidentLastNames = studentsWithRoles
    .filter(student => student.role === 'Full Stack Resident')
    .map(student => student.lastName);
  console.log(fullStackResidentLastNames);
  