



-- Step 2: Create the 'items' table
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price INT
);

-- Step 3: Create the 'customers' table
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(255),
    lastname VARCHAR(255)
);

-- Step 4: Insert data into the 'items' table
INSERT INTO items (name, price) VALUES
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

-- Step 5: Insert data into the 'customers' table
INSERT INTO customers (firstname, lastname) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

-- Step 6: SQL Queries

-- Fetch all items
SELECT * FROM items;

-- Fetch items with a price above 80
SELECT * FROM items WHERE price > 80;

-- Fetch items with a price below or equal to 300
SELECT * FROM items WHERE price <= 300;

-- Fetch customers whose last name is 'Smith'
SELECT * FROM customers WHERE lastname = 'Smith';

-- Fetch customers whose last name is 'Jones'
SELECT * FROM customers WHERE lastname = 'Jones';

-- Fetch customers whose first name is not 'Scott'
SELECT * FROM customers WHERE firstname != 'Scott';

