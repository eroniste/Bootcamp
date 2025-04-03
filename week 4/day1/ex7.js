(function(userName) {
    const navbar = document.querySelector('nav');
    const div = document.createElement('div');
    div.innerHTML = `Welcome, ${userName}! <img src="profile.jpg" alt="Profile Picture">`;
    navbar.appendChild(div);
  })('John');