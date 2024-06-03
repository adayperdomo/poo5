import sqlite3

SQLMDLCREATE = """
    CREATE TABLE IF NOT EXITS citas (
    id INTERGER PRIMARY KEY AUTOINCREMENT,
    cita TEXT NOT NULL
)
"""

con = sqlite3.connect("citas.db")

con.close()