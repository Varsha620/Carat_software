import sqlite3

def get_connection():
    return sqlite3.connect("goldshop.db")

def create_tables():
    conn = get_connection()
    c = conn.cursor()

    # ITEMS TABLE
    c.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            price REAL,
            weight REAL
        )
    """)

    # CUSTOMERS
    c.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            address TEXT
        )
    """)

    # EMPLOYEES
    c.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT,
            salary REAL
        )
    """)

    # BILL MASTER
    c.execute("""
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            date TEXT,
            total REAL,
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        )
    """)

    # BILL ITEMS
    c.execute("""
        CREATE TABLE IF NOT EXISTS bill_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bill_id INTEGER,
            item_id INTEGER,
            qty INTEGER,
            price REAL,
            FOREIGN KEY(bill_id) REFERENCES bills(id),
            FOREIGN KEY(item_id) REFERENCES items(id)
        )
    """)

    conn.commit()
    conn.close()

# Run this file once to create DB
if __name__ == "__main__":
    create_tables()
    print("Database created!")
