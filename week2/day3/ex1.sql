select * from language;
SELECT film.title, film.description, language.name AS language
FROM film
INNER JOIN language ON film.language_id = language.language_id;
SELECT film.title, film.description, language.name AS language
FROM language
LEFT JOIN film ON film.language_id = language.language_id;

CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO new_film (name) VALUES ('Inception'), ('The Matrix'), ('Interstellar');


CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(255) NOT NULL,
    score INT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES 
(1, 1, 'Mind-blowing movie', 10, 'This film was an absolute masterpiece!'),
(2, 2, 'Great Action', 9, 'Loved the action sequences and the concept!');


DELETE FROM new_film WHERE id = 1;


SELECT * FROM customer_review;

