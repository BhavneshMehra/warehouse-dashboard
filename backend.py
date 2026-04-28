from fastapi import FastAPI
import sqlite3
import random
from datetime import datetime

app = FastAPI()
DB = "warehouse.db"

PRODUCTS = ["Laptop", "Phone", "Headphones", "Shoes"]

# ---------- DB CONNECTION ----------
def get_conn():
    return sqlite3.connect(DB, check_same_thread=False)


# ---------- INIT DB ----------
def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        status TEXT,
        created_at TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        product TEXT PRIMARY KEY,
        stock INTEGER
    )
    """)

    for p in PRODUCTS:
        c.execute("INSERT OR IGNORE INTO inventory VALUES (?, ?)", (p, 100))

    conn.commit()
    conn.close()


init_db()


# ---------- GENERATE ORDER ----------
def generate_order():
    conn = get_conn()
    c = conn.cursor()

    product = random.choice(PRODUCTS)
    qty = random.randint(1, 5)

    # get stock
    c.execute("SELECT stock FROM inventory WHERE product=?", (product,))
    stock = c.fetchone()[0]

    # ---------- ORDER LOGIC ----------
    if stock >= qty:
        c.execute(
            "UPDATE inventory SET stock=stock-? WHERE product=?",
            (qty, product)
        )

        # simulate lifecycle
        status = random.choices(
            ["Pending", "Packed", "Shipped"],
            weights=[1, 3, 2]
        )[0]
    else:
        status = "Pending"

    # insert order
    c.execute("""
    INSERT INTO orders (product, quantity, status, created_at)
    VALUES (?, ?, ?, ?)
    """, (product, qty, status, datetime.now().isoformat()))

    conn.commit()
    conn.close()


# ---------- LOW STOCK CHECK ----------
def get_low_stock_items():
    conn = get_conn()
    c = conn.cursor()

    c.execute("SELECT product FROM inventory WHERE stock < 20")
    low_stock = [row[0] for row in c.fetchall()]

    conn.close()
    return low_stock


# ---------- API: GENERATE ----------
@app.get("/generate")
def generate():
    generate_order()
    return {"message": "Order generated"}


# ---------- API: DASHBOARD ----------
@app.get("/dashboard")
def dashboard():
    conn = get_conn()
    c = conn.cursor()

    c.execute("SELECT * FROM orders ORDER BY id DESC LIMIT 20")
    orders = c.fetchall()

    c.execute("SELECT * FROM inventory")
    inventory = c.fetchall()

    conn.close()

    return {
        "orders": orders,
        "inventory": inventory,
        "low_stock": get_low_stock_items()
    }


# ---------- API: RESET (optional for demo) ----------
@app.get("/reset")
def reset():
    conn = get_conn()
    c = conn.cursor()

    c.execute("DELETE FROM orders")

    for p in PRODUCTS:
        c.execute("UPDATE inventory SET stock=100 WHERE product=?", (p,))

    conn.commit()
    conn.close()

    return {"message": "System reset complete"}