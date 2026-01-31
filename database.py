# AI usage in this file
# - used to write some sql queries
# - used to write function descriptions because i ain't writing that myself
import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS channels (
  id TEXT PRIMARY KEY,
  number INTEGER,
  user TEXT,
  type TEXT             
)               
""")

def add_channel(id: str, type: str):
  """Add a new channel to the database with initial count of 0.
  
  Args:
    id: The channel ID
    type: The channel type (e.g., 'counting', 'reverse')
  """
  cursor.execute(
    "INSERT INTO channels (id, number, user, type) VALUES (?, ?, ?, ?)",
    (id, 0, None, type)
  )
  conn.commit()

def get_type(id: str) -> str | None:
  """Get the type of a channel.
  
  Args:
    id: The channel ID
    
  Returns:
    The channel type, or None if channel doesn't exist
  """
  cursor.execute(
    "SELECT type FROM channels WHERE id = ?",
    (id)
  )
  result = cursor.fetchone()
  return result[0] if result else None

def set_type(id: str, type: str):
  """Update the type of a channel.
  
  Args:
    id: The channel ID
    type: The new channel type
  """
  cursor.execute(
    "UPDATE channels SET type = ? WHERE id = ?",
    (type, id)
  )
  conn.commit()

def get_progress(id: str) -> tuple[str, int] | None:
  """Get the current counting progress for a channel.
  
  Args:
    id: The channel ID
    
  Returns:
    A tuple of (last_user, current_number), or None if channel doesn't exist
  """
  cursor.execute(
    "SELECT user, number FROM channels WHERE id = ?",
    (id,)
  )
  result = cursor.fetchone()
  return result if result else None

def set_progress(id: str, user: str, number: int):
  """Update the counting progress for a channel.
  
  Args:
    id: The channel ID
    user: The ID of the user who posted the last count
    number: The current count number
  """
  cursor.execute(
    "UPDATE channels SET user = ?, number = ? WHERE id = ?",
    (user, number, id)
  )
  conn.commit()