import sqlite3

connection = sqlite3.connect("nilearn.db")

resources = [
    (
        "Mathematics Past Paper 2024",
        "Mathematics",
        "Past Paper",
        2024,
        "Grade 12 Mathematics past examination paper.",
        "math_2024.pdf"
    ),

    (
        "Physics Past Paper 2024",
        "Physics",
        "Past Paper",
        2024,
        "Grade 12 Physics past examination paper",
        "physics_2024.pdf"

    ),

    (
        "English Past Paper 2024",
        "English",
        "Past Paper",
        2024,
        "Grade 12 English past examination paper",
        "english_2024.pdf"

    )
]

connection.executemany("""
    INSERT INTO resources
    (title, subject, resource_type, year, description, file_path)
    VALUES (?, ?, ?, ?, ?, ?)
    """, resources
)

connection.commit()
connection.close()

print("Sample resources added")
