import sqlite3

SQLMDLCREATE = """
    CREATE TABLE IF NOT EXISTS citas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cita TEXT NOT NULL
)
"""

con = sqlite3.connect("citas.db", autocommit=True)

con.execute(SQLMDLCREATE)

SQLDDINSERT = """
    INSERT INTO citas(cita) Values ('La vida es bella')
"""

con.execute(SQLDDINSERT)
#con.commit()

SQLDDSELECT = """
    SELECT * FROM citas
"""

res = con.execute(SQLDDSELECT)
print(res.fetchall())

con.close()