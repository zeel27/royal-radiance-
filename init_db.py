import sqlite3

conn = sqlite3.connect('database.db')

# Create products table
conn.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price TEXT NOT NULL,
    category TEXT NOT NULL,
    image TEXT
)
''')

# Create messages table
conn.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL
)
''')

# Optional: Insert sample products
conn.execute("INSERT INTO products (name, price, category, image) VALUES ('Royal Sherwani', '$199', 'Men', 'sherwani.jpg')")
conn.execute("INSERT INTO products (name, price, category, image) VALUES ('Bridal Lehenga', '$399', 'Women', 'lehenga.jpg')")
conn.execute("INSERT INTO products (name, price, category, image) VALUES ('Kurta Set', '$99', 'Children', 'kurta.jpg')")

conn.commit()
conn.close()

print("Database initialized.")
