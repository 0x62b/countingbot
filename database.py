import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS channels (
  id TEXT PRIMARY KEY,
  number INTEGER,
  user TEXT
  type TEXT               
)               
""")