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

def create_tag(new_tag):
    """Creating a new tag then adding it to 'Tags' table in db.sqlite3"""
    with sqlite3.connect('./db.sqlite3') as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        INSERT INTO Tags
            ( label )
        VALUES
            ( ? );
        """, (new_tag['label'], ))
        
        id = db_cursor.lastrowid
        new_tag['id'] = id
    
    return json.dumps(new_tag)
