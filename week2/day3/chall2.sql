CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE product_orders (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    quantity INT NOT NULL CHECK (quantity > 0),
    FOREIGN KEY (order_id) REFERENCES product_orders(id) ON DELETE CASCADE
);

-- Function to get total price for a given order
CREATE FUNCTION get_order_total(orderId INT) RETURNS DECIMAL(10,2) AS $$
DECLARE total DECIMAL(10,2);
BEGIN
    SELECT COALESCE(SUM(price * quantity), 0) INTO total
    FROM items
    WHERE order_id = orderId;
    
    RETURN total;
END;
$$ LANGUAGE plpgsql;

-- Function to get total price for a given order of a specific user
CREATE FUNCTION get_user_order_total(userId INT, orderId INT) RETURNS DECIMAL(10,2) AS $$
DECLARE total DECIMAL(10,2);
BEGIN
    SELECT COALESCE(SUM(i.price * i.quantity), 0) INTO total
    FROM items i
    JOIN product_orders o ON i.order_id = o.id
    WHERE o.id = orderId AND o.user_id = userId;
    
    RETURN total;
END;
$$ LANGUAGE plpgsql;
