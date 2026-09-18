import sqlite3
import os

connection = sqlite3.connect("nilearn.db")

resources = connection.execute(
    "SELECT id, file_path FROM resources"
).fetchall()


for resource in resources:
    file_path = "uploads/" + resource[1]

    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)

        connection.execute(
            "UPDATE resources SET file_size = ? WHERE id = ?",
            (file_size, resource[0])
        )

connection.commit()
connection.close()
