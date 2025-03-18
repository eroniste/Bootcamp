CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,  -- Changed from 'age' to 'birth_date'
    number_oscars SMALLINT NOT NULL
);

INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
VALUES ('Matt', 'Damon', '1970-10-08', 5);

INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
VALUES ('George', 'Clooney', '1961-05-06', 2);

SELECT COUNT(*) FROM actors;
INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
VALUES (NULL, NULL, NULL, NULL);

