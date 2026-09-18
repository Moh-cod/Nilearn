import sqlite3

connection = sqlite3.connect("nilearn.db")

connection.execute(
    "ALTER TABLE resources ADD COLUMN file_size INTEGER"
)

connection.commit()
connection.close()

print("file_size column added")
