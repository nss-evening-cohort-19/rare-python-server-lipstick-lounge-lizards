import sqlite3
import json
from models import Tags

def get_all_tags():
    """Get all tags"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tags t
        """)
      
        tags = []
      
        dataset = db_cursor.fetchall()
      
        for row in dataset:
            tag = Tags(row['id'], row['label'])
          
            tags.append(tag.__dict__)
  
    return json.dumps(tags)
