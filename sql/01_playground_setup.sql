-- ====================================================================
-- Part 1: Setting Up a Playground (Analytics Made Simple)
-- Full Tutorial: https://analyticsmadesimple.com/tutorials/tutorial-1-setting-up-sql/
-- ====================================================================

-- 1. Create Customers Table
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    signup_date DATE NOT NULL,
    country TEXT NOT NULL
);

-- 2. Create Orders Table
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
    status TEXT NOT NULL,
    total_amount NUMERIC(10, 2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- 3. Seed Sample Customers
INSERT INTO customers (customer_id, first_name, last_name, email, signup_date, country) VALUES
(1, 'Alice', 'Morgan', 'alice.m@example.com', '2024-01-15', 'USA'),
(2, 'Bob', 'Chen', 'bob.chen@example.com', '2024-02-01', 'Canada'),
(3, 'Carla', 'Gomez', 'carla.g@example.com', '2024-02-14', 'USA'),
(4, 'David', 'Kim', 'david.k@example.com', '2024-03-10', 'UK'),
(5, 'Elena', 'Rostova', 'elena.r@example.com', '2024-03-22', 'Germany');

-- 4. Seed Sample Orders
INSERT INTO orders (order_id, customer_id, order_date, status, total_amount) VALUES
(101, 1, '2024-02-01', 'completed', 149.99),
(102, 1, '2024-03-15', 'completed', 89.50),
(103, 2, '2024-02-18', 'completed', 45.00),
(104, 3, '2024-03-01', 'cancelled', 210.00),
(105, 3, '2024-03-20', 'completed', 320.00),
(106, 4, '2024-03-25', 'pending', 75.25);

-- 5. Quick Verification
SELECT 'Playground schema created successfully!' AS status;
SELECT count(*) AS total_customers FROM customers;
SELECT count(*) AS total_orders FROM orders;
