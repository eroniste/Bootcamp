

const allBooks = [
    {title: "Book 1", author: "Author 1", image: "url1", alreadyRead: true},
    {title: "Book 2", author: "Author 2", image: "url2", alreadyRead: false}
];

const listBooks = document.querySelector(".listBooks");

allBooks.forEach(book => {
    const bookDiv = document.createElement("div");
    const title = document.createElement("h3");
    title.textContent = `${book.title} written by ${book.author}`;
    const image = document.createElement("img");
    image.src = book.image;
    image.style.width = "100px";

    bookDiv.appendChild(title);
    bookDiv.appendChild(image);
    
    if (book.alreadyRead) {
        bookDiv.style.color = "red";
    }

    listBooks.appendChild(bookDiv);
});
