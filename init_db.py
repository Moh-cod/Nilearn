import sqlite3

connection = sqlite3.connect("nilearn.db")

connection.execute("""
CREATE TABLE IF NOT EXISTS resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    subject TEXT NOT NULL,
    resource_type TEXT NOT NULL,
    year INTEGER,
    description TEXT,
    file_path TEXT,
    file_size INTEGER
    )
""")

connection.commit()
connection.close()

print("Database initialized.")
