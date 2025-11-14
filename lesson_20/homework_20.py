import os
import sqlite3

if os.path.exists("shop.db"):
    os.remove("shop.db")

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
""")

cursor.executescript("""
INSERT INTO categories (name) VALUES
('Electronics'),
('Clothing'),
('Books'),
('Accesories');

INSERT INTO products (name, description, price, category_id) VALUES
('Smartphone', 'Iphone', 699.99, 1),
('Laptop', 'Asus', 1199.00, 1),
('Mouse', 'Razer', 25.50, 2),
('Jacket', 'No name ) ', 49.90, 2),
('Book', 'Записки Українського сумашедшего', 15.00, 3),
('Accesories', 'Smth I have no idea what', 120.00, 4);
""")

cursor.execute("""
SELECT 
    p.id AS product_id,
    p.name AS product_name,
    p.description,
    p.price,
    c.name AS category_name
FROM products p
JOIN categories c ON p.category_id = c.id;
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()