import sqlite3

conn = sqlite3.connect('predictions.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sqft INTEGER,
        bedrooms INTEGER,
        predicted_price REAL
    )
""")

conn.commit()
conn.close()

print("✅ Database initialized.")
