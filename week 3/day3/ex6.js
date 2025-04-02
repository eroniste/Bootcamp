

const navBar = document.getElementById("navBar");
navBar.setAttribute("id", "socialNetworkNavigation");

const logoutItem = document.createElement("li");
const logoutText = document.createTextNode("Logout");
logoutItem.appendChild(logoutText);
navBar.querySelector("ul").appendChild(logoutItem);

const firstItem = navBar.querySelector("ul").firstElementChild;
const lastItem = navBar.querySelector("ul").lastElementChild;
console.log(firstItem.textContent);
console.log(lastItem.textContent);
