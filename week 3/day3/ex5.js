// exercise5.js

const container = document.getElementById("container");
console.log(container);

const firstList = document.querySelectorAll(".list")[0];
firstList.children[1].textContent = "Richard";

const secondList = document.querySelectorAll(".list")[1];
secondList.children[1].remove();

const listItems = document.querySelectorAll(".list li");
listItems[0].textContent = "YourName";
listItems[2].textContent = "YourName";

document.querySelectorAll(".list").forEach(list => {
    list.classList.add("student_list");
});
firstList.classList.add("university", "attendance");

container.style.backgroundColor = "lightblue";
container.style.padding = "10px";

const danElement = document.querySelector("li:contains('Dan')");
if (danElement) {
    danElement.style.display = "none";
}

const richardElement = document.querySelector("li:contains('Richard')");
if (richardElement) {
    richardElement.style.border = "2px solid red";
}

document.body.style.fontSize = "18px";

if (container.style.backgroundColor === "lightblue") {
    alert("Hello x and y");
}
