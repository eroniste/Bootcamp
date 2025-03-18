
SELECT * FROM customer;

SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customer;

SELECT DISTINCT create_date FROM customer;

SELECT * FROM customer ORDER BY first_name DESC;

SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;

SELECT a.address, a.phone
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
WHERE a.district = 'Texas';

SELECT * FROM film WHERE film_id IN (15, 150);

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = 'Your Favorite Movie';

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title LIKE 'Yo%';

SELECT * FROM film
ORDER BY rental_rate ASC
FETCH FIRST 10 ROWS ONLY;

SELECT * FROM (
    SELECT film_id, title, rental_rate, ROW_NUMBER() OVER (ORDER BY rental_rate ASC) AS row_num
    FROM film
) AS ranked_films
WHERE row_num > 10 AND row_num <= 20;

SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id;

SELECT * FROM film
WHERE film_id NOT IN (
    SELECT film_id FROM inventory
);

SELECT ci.city, co.country
FROM city ci
JOIN country co ON ci.country_id = co.country_id;

SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
JOIN staff s ON p.staff_id = s.staff_id
ORDER BY s.staff_id;
