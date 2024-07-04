create database brewhub;
use brewhub;

CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    email VARCHAR(255) NOT NULL
);


CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50) NOT NULL,
    item VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);


CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);


CREATE TABLE Order_Items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    item_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);


INSERT INTO Products (category, item, price) VALUES 
('Coffees', 'Latte (cold)', 450.00),
('Coffees', 'Cappuccino', 500.00),
('Coffees', 'Espresso', 300.00),
('Coffees', 'Mocha', 475.00),
('Coffees', 'Americano', 350.00),
('Coffees', 'Flat White', 480.00),
('Coffees', 'Macchiato', 400.00),
('Coffees', 'Affogato', 550.00),
('Coffees', 'Irish Coffee', 600.00),
('Coffees', 'Vienna Coffee', 520.00);

INSERT INTO Products (category, item, price) VALUES 
('Iced Teas & Lemonades', 'Strawberry Lemonade', 450.00),
('Iced Teas & Lemonades', 'Berry Lemonade', 500.00),
('Iced Teas & Lemonades', 'Classic Lemonade', 300.00),
('Iced Teas & Lemonades', 'Citrus Ice Tea', 475.00),
('Iced Teas & Lemonades', 'Lemon Cold Brew', 350.00),
('Iced Teas & Lemonades', 'Peach Iced Tea', 480.00),
('Iced Teas & Lemonades', 'Mint Lemonade', 420.00),
('Iced Teas & Lemonades', 'Watermelon Cooler', 550.00),
('Iced Teas & Lemonades', 'Cucumber Mint Cooler', 600.00),
('Iced Teas & Lemonades', 'Blueberry Lemonade', 520.00);

INSERT INTO Products (category, item, price) VALUES 
('Milkshakes', 'Chocolate Milkshake', 550.00),
('Milkshakes', 'Vanilla Milkshake', 500.00),
('Milkshakes', 'Strawberry Milkshake', 520.00),
('Milkshakes', 'Caramel Milkshake', 580.00),
('Milkshakes', 'Banana Milkshake', 450.00),
('Milkshakes', 'Oreo Milkshake', 600.00),
('Milkshakes', 'Peanut Butter Milkshake', 570.00),
('Milkshakes', 'Coffee Milkshake', 520.00),
('Milkshakes', 'Mint Chocolate Chip Milkshake', 590.00),
('Milkshakes', 'Nutella Milkshake', 550.00);

INSERT INTO Products (category, item, price) VALUES 
('Snacks', 'French Fries', 200.00),
('Snacks', 'Nachos', 250.00),
('Snacks', 'Chicken Wings', 350.00),
('Snacks', 'Garlic Bread', 180.00),
('Snacks', 'Onion Rings', 220.00),
('Snacks', 'Mozzarella Sticks', 280.00),
('Snacks', 'Poutine', 300.00),
('Snacks', 'Spring Rolls', 210.00),
('Snacks', 'Bruschetta', 240.00),
('Snacks', 'Hummus Platter', 270.00);
